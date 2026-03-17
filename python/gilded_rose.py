# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdateStrategy:
    """Base strategy for updating one item for one day."""

    def update(self, item):
        raise NotImplementedError

    def increase_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item, amount):
        item.quality = max(0, item.quality - amount)

    def decrease_sell_in(self, item):
        item.sell_in -= 1


class RegularItemStrategy(ItemUpdateStrategy):
    def update(self, item):
        degrade_amount = 1
        if item.sell_in <= 0:
            degrade_amount = 2

        self.decrease_quality(item, degrade_amount)
        self.decrease_sell_in(item)


class AgedBrieStrategy(ItemUpdateStrategy):
    def update(self, item):
        increase_amount = 1
        if item.sell_in <= 0:
            increase_amount = 2

        self.increase_quality(item, increase_amount)
        self.decrease_sell_in(item)


class BackstagePassStrategy(ItemUpdateStrategy):
    def update(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            self.increase_quality(item, 3)
        elif item.sell_in <= 10:
            self.increase_quality(item, 2)
        else:
            self.increase_quality(item, 1)

        self.decrease_sell_in(item)


class SulfurasStrategy(ItemUpdateStrategy):
    def update(self, item):
        return


class ConjuredItemStrategy(ItemUpdateStrategy):
    def update(self, item):
        degrade_amount = 2
        if item.sell_in <= 0:
            degrade_amount = 4

        self.decrease_quality(item, degrade_amount)
        self.decrease_sell_in(item)


class ItemUpdateStrategyFactory:
    def __init__(self):
        self.default_strategy = RegularItemStrategy()
        self.conjured_strategy = ConjuredItemStrategy()
        self.named_strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        }

    def get_strategy(self, item):
        # Conjured is treated as a family so future conjured names can reuse the rule.
        if item.name.startswith("Conjured"):
            return self.conjured_strategy

        return self.named_strategies.get(item.name, self.default_strategy)


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.strategy_factory = ItemUpdateStrategyFactory()

    def update_quality(self):
        for item in self.items:
            strategy = self.strategy_factory.get_strategy(item)
            strategy.update(item)
