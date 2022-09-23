import os
import orjson
from typing import Iterator

SAVE: bool = True
FROM_SAVED: bool = False

ROOT_PATH: str = os.path.dirname(os.path.abspath(__file__))

no_ein_data: str = open(os.path.join(
    ROOT_PATH, 'strand_no_ein.txt'), 'r').read()
ein_data: str = open(os.path.join(
    ROOT_PATH, 'strand_ein_goat_savage_mem.txt'), 'r').read()
ein_data_1: str = open(os.path.join(
    ROOT_PATH, 'strand_ein_rhoa_retch_mem.txt'), 'r').read()
spider_found_data: str = open(os.path.join(
    ROOT_PATH, 'strand_spider_mem.txt'), 'r').read()


spider_found_data_other_map: str = open(os.path.join(
    ROOT_PATH, 'acid_cavern_spider_mem.txt'), 'r').read()

other_map_no_ein: str = open(os.path.join(
    ROOT_PATH, 'other_map_no_ein.txt'), 'r').read()
other_map_no_ein_1: str = open(os.path.join(
    ROOT_PATH, 'other_map_no_ein_1.txt'), 'r').read()


def get_texture_resources(content: str) -> Iterator[str]:
    for line in content.splitlines():
        if 'TextureResource/' in line and line != 'TextureResource/':
            yield line


if not FROM_SAVED:

    no_ein_textures: list[str] = list(get_texture_resources(no_ein_data))
    ein_data_textures: list[str] = list(get_texture_resources(ein_data))
    ein_data_1_textures: list[str] = list(get_texture_resources(ein_data_1))
    spider_found_data_textures: list[str] = list(get_texture_resources(spider_found_data))  # noqa
    spider_found_data_other_map_textures: list[str] = list(get_texture_resources(spider_found_data_other_map))  # noqa
    other_map_no_ein_textures: list[str] = list(get_texture_resources(other_map_no_ein))  # noqa
    other_map_no_ein_1_textures: list[str] = list(get_texture_resources(other_map_no_ein_1))  # noqa

else:

    with open(os.path.join(ROOT_PATH, 'data.json'), 'r') as handle:
        data: dict[str, list[str]] = orjson.loads(handle.read())

    no_ein_textures: list[str] = data['no_ein_textures']
    ein_data_textures: list[str] = data['ein_data_textures']
    ein_data_1_textures: list[str] = data['ein_data_1_textures']
    spider_found_data_textures: list[str] = data['spider_found_data_textures']
    spider_found_data_other_map_textures: list[str] = data['spider_found_data_other_map_textures']
    other_map_no_ein_textures: list[str] = data['other_map_no_ein_textures']
    other_map_no_ein_1_textures: list[str] = data['other_map_no_ein_1_textures']


if SAVE:
    with open(os.path.join(ROOT_PATH, 'data.json'), 'wb') as handle:
        handle.write(orjson.dumps({
            "no_ein_textures": no_ein_textures,
            "ein_data_textures": ein_data_textures,
            "ein_data_1_textures": ein_data_1_textures,
            "spider_found_data_textures": spider_found_data_textures,
            "spider_found_data_other_map_textures": spider_found_data_other_map_textures,
            "other_map_no_ein_textures": other_map_no_ein_textures,
            "other_map_no_ein_1_textures": other_map_no_ein_1_textures
        }))

map_info: list[str] = list()

for texture in no_ein_textures:
    if (
        texture in ein_data_1_textures
        and texture in ein_data_textures
        and texture in spider_found_data_textures
        and texture in spider_found_data_other_map_textures
    ):
        map_info.append(texture)

for texture in map_info:
    if texture not in ein_data_textures or texture not in ein_data_1_textures:
        print(f'WARNING!!!. LOOKS LIKE MAP_INFO PARSED WRONG -> "{texture}"')


same_data_of_ein: list[str] = list()

for texture in ein_data_textures:
    if texture in ein_data_1_textures and texture in spider_found_data_textures and spider_found_data_other_map_textures:
        same_data_of_ein.append(texture)

possible_spider_textures: list[str] = list()

for texture in spider_found_data_textures:
    if (
        texture not in map_info
        and texture not in same_data_of_ein
        and texture not in ein_data_textures
        and texture not in ein_data_1_textures
        and texture not in no_ein_textures
        and texture not in other_map_no_ein_textures
        and texture not in other_map_no_ein_1_textures
        and texture in spider_found_data_other_map_textures
    ):
        possible_spider_textures.append(texture)


# print(possible_spider_textures)

for texture in possible_spider_textures:
    if texture in no_ein_textures:
        print(texture)

value = 'TextureResource/f8e3b071f2bcea6af37213c65abd1d6d4fdae790c965b6b8e7195c722eea78b0'

print(value in ein_data_1_textures)
