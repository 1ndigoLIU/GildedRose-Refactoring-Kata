# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def update_item(self, name, sell_in, quality, days=1):
        item = Item(name, sell_in, quality)
        gilded_rose = GildedRose([item])

        for _ in range(days):
            gilded_rose.update_quality()

        return item

    def test_normal_items_degrade_by_one_before_sell_date(self):
        item = self.update_item("+5 Dexterity Vest", 10, 20)

        self.assertEqual(9, item.sell_in)
        self.assertEqual(19, item.quality)

    def test_normal_items_degrade_twice_as_fast_after_sell_date(self):
        item = self.update_item("Elixir of the Mongoose", 0, 10)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(8, item.quality)

    def test_quality_is_never_negative(self):
        item = self.update_item("+5 Dexterity Vest", 5, 0)

        self.assertEqual(0, item.quality)

    def test_aged_brie_increases_in_quality(self):
        item = self.update_item("Aged Brie", 2, 0)

        self.assertEqual(1, item.sell_in)
        self.assertEqual(1, item.quality)

    def test_aged_brie_quality_is_capped_at_fifty(self):
        item = self.update_item("Aged Brie", 0, 49)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_sulfuras_never_changes(self):
        item = self.update_item("Sulfuras, Hand of Ragnaros", 0, 80)

        self.assertEqual(0, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_backstage_passes_increase_by_two_when_ten_days_or_less(self):
        item = self.update_item("Backstage passes to a TAFKAL80ETC concert", 10, 20)

        self.assertEqual(9, item.sell_in)
        self.assertEqual(22, item.quality)

    def test_backstage_passes_drop_to_zero_after_concert(self):
        item = self.update_item("Backstage passes to a TAFKAL80ETC concert", 0, 20)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_conjured_items_degrade_twice_as_fast_before_sell_date(self):
        item = self.update_item("Conjured Mana Cake", 3, 6)

        self.assertEqual(2, item.sell_in)
        self.assertEqual(4, item.quality)

    def test_conjured_items_degrade_four_times_as_fast_after_sell_date(self):
        item = self.update_item("Conjured Mana Cake", 0, 10)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(6, item.quality)


if __name__ == "__main__":
    unittest.main()
