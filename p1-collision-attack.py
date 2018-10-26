#!/usr/bin/env python3
import hashlib # check the md5 of the text

def next(sub_book_item_idx, sub_book_size):
    item_num = len(sub_book_item_idx)
    for idx in range(item_num):
        sub_book_item_idx[idx] = (sub_book_item_idx[idx] + 1) % sub_book_size[idx]
        if sub_book_item_idx[idx] != 0:
            break
    return sub_book_item_idx, sum(sub_book_item_idx) == 0

def form_text(format_text, sub_book, sub_book_item_idx):
    text = format_text.format(\
    sub_book[0][sub_book_item_idx[0]],
    sub_book[1][sub_book_item_idx[1]],
    sub_book[2][sub_book_item_idx[2]],
    sub_book[3][sub_book_item_idx[3]],
    sub_book[4][sub_book_item_idx[4]],
    sub_book[5][sub_book_item_idx[5]],
    sub_book[6][sub_book_item_idx[6]],
    sub_book[7][sub_book_item_idx[7]],
    sub_book[8][sub_book_item_idx[8]],
    sub_book[9][sub_book_item_idx[9]],
    sub_book[10][sub_book_item_idx[10]],
    sub_book[11][sub_book_item_idx[11]],
    sub_book[12][sub_book_item_idx[12]],
    sub_book[13][sub_book_item_idx[13]],
    sub_book[14][sub_book_item_idx[14]],
    sub_book[15][sub_book_item_idx[15]],
    sub_book[16][sub_book_item_idx[16]],
    sub_book[17][sub_book_item_idx[17]],
    sub_book[18][sub_book_item_idx[18]],
    sub_book[19][sub_book_item_idx[19]]
    )
    return text


org_text = """More efficient attacks are possible by employing cryptanalysis to specific hash functions. When a collision attack is discovered and is found to be faster than a birthday attack, a hash function is often denounced as "broken". The NIST hash function competition was largely induced by published collision attacks against two very commonly used hash functions, MD5 and SHA-1. The collision attacks against MD5 have improved so much that, as of 2007, it takes just a few seconds on a regular computer. Hash collisions created this way are usually constant length and largely unstructured, so cannot directly be applied to attack widespread document formats or protocols."""

format_text = """{} attacks are {} by {} cryptanalysis to {} hash functions. When a collision attack is {} and is {} to be {} than a birthday attack, a hash function is often {} {} "broken". The NIST hash function competition was {} {} by published collision attacks against two very {} used hash functions, {}. The collision attacks against MD5 have improved so much that, as of 2007, it takes just a {} seconds on a {} computer. Hash collisions {} this way are usually {} length and {} unstructured, so {} be {} to attack widespread document formats or protocols."""

sub_book = [
["More efficient", "High efficient"],
["possible", "practical"],
["employing", "applying", "using", "making use of", "exploiting", "utilizing"],
["specific", "perticular", "certain"],
["discovered", "uncovered"],
["found", "realized", "shown", "proved"],
["faster", "quicker"],
["denounced", "declared", "considered", "regarded"],
["as", "to be"],
["largely", "mainly"],
["induced", "inspired"],
["commonly", "widely"],
["MD5 and SHA-1", "SHA-1 and MD5"],
["few", "couple of"],
["regular", "common"],
["created", "generated"],
["constant", "fixed"],
["largely", "almostly"],
["cannot directly", "impractical to"],
["applied", "deployed", "used"]
]

sub_book_size = [len(i) for i in sub_book]
sub_book_item_idx = [0] * len(sub_book)

md5_item_dict = {}

is_end = False
is_found = False
round_idx = 0
while not is_end:
    text = form_text(format_text, sub_book, sub_book_item_idx)
    text_md5 = hashlib.md5(text.encode()).hexdigest()

    # manually change it to 64-bit hash
    # text_md5 = text_md5 [-16:] # 256 bit hash  # currently cannot find collision
    # text_md5 = text_md5 [-8:] # 128 bit hash
    text_md5 = text_md5 [-4:] # 64 bit hash

    if text_md5 not in md5_item_dict:
        md5_item_dict[text_md5] = [round_idx, sub_book_item_idx.copy()]
    else:
        is_found = True
        print("collision found after {} attempts!".format(len(md5_item_dict)+1))
        prev_text = form_text(format_text, sub_book, md5_item_dict[text_md5][1])
        print(sub_book_item_idx)
        print(md5_item_dict[text_md5][1])
        print(text)
        print(prev_text)
        print(text_md5)
        break
    sub_book_item_idx, is_end = next(sub_book_item_idx, sub_book_size)
    round_idx += 1
    # break # debug use only

if not is_found:
    print("collision not found")
