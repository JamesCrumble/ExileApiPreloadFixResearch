import os
from turtle import pos

possible_spider_textures: list[str] = [
    'TextureResource/5c1b36123d91854c7e3fa48f03bf38b2b6ace2b9df3ff6455349d48aea57ca4f',
    'TextureResource/0333a25c035d87835f59c6e86299713c869ff15495d9a42eadde1ab8df3c057f',
    'TextureResource/7629c99738bd304814e595ad5fdadd0a02c0b91f9cf8eff4cdf0c2976a1fb203',
    'TextureResource/222e437ead6f49cec52ed627cb2cc03c147205e315a8d4659b2519d94406a136',
    'TextureResource/a4d0387965e0253234fcfecfe85989c11583d89e2ab97379a345dc9c72ede4f9',
    'TextureResource/d28b8a1f80d8696fdccf5c0e1e0dbe69407800643b438719ccbad135124dd1b6',
    'TextureResource/e65da52ac0c9366000cb330a84b2444355b3cc0a0243dc33862e3646530737e1',
    'TextureResource/3b3e47218ce8654dc5d4e5442dd28ec8e66003366d8aae4d55afca664eff7a35',
    'TextureResource/587ebb7d0fb6923401bf2e9c36b7d19bae480285fe9f2eb18b8cf7b881eafbab',
    'TextureResource/a6edc0ece1977e6b522c6c629b70df33a40dc942e6d7a3dfe9c2a39887fb619d',
    'TextureResource/2126464d2babe9f06beeebb6a63cc778e7aa6eed4eba144365ed75db8c2d75a4',
    'TextureResource/d076cd22f5795bebf85d12fbbb98dc21ece3e020ca994d35c64cc4e06904e352',
    'TextureResource/15ea599a5b58d81892ad247d1909bd12b7443b365105bdfaa288065590ba4ab1',
    'TextureResource/37c17b35bc692babd72f7edeb72aff699a18be39b91350791acced9fdbda38e1',
    'TextureResource/1eed8e9c5e68d8f8389840422d19c13bcd763c8eff63da69a261ad70015054cb',
    'TextureResource/35996e0b6d8997bdc9c789e7803349b6eb607b04c01b49bdc3483f4c71f64bc5',
    'TextureResource/994bbf0f079304037b94f519fb2ecec1f17711222de82d00c4e9b237872dd343',
    'TextureResource/03f4ab90ccb2ceac0c2849ecf66a4eccd765850bd8cedcc44efe32d02b20ce48',
    'TextureResource/6699787c6b244c4f48b677cde6297ebf0f5415013ae0c330a45f45fef38f958b',
    'TextureResource/cc05618627ebd3adefcf1aed645b00d8b2f6712dc937fa88ff6bc72b3974c48d',
    'TextureResource/0c6b6f8d176b480f0769dc26042d97b50eeed9dcd6a95c6611418f4962412e6e',
    'TextureResource/08ad3a65794ad4ba5b783ca0ea137f01d0b1453267069db0f93d7bcc0bd1a46c',
    'TextureResource/4d1e817dc4e15edf5909095105efcbb021f7ccbab6e09c7f964900719f07ccea',
    'TextureResource/d88119b0a1cf95e232e683bc5961419b1a937753bd4350a1030204f9ae84de34',
    'TextureResource/e1a2b22d9b016395fd78968b1104074cd2b0de4e1b2c076e180142f13e85edd5',
    'TextureResource/b43e6513b2e22d58843e5e71e7561d6e1e8fae81474dc6c4e2baa59e2ad8c96b',
    'TextureResource/a3f6919d78e4ddaf3d42bf19e6cbc16789f1cd85cc597ffa7cb290684ee48f70',
    'TextureResource/c1b660463d33bbad9016623f55bb571e80d77503ab76c3b6622ff474777d352e',
    'TextureResource/5c12fb5cd6e5f1465062f92fd9536e0778df628908da3338847ceba85b83ca3d',
    'TextureResource/47b3e1d443f6118215f321021dc6aec9fa268dc429dc7b326b93098407f7a7e7',
    'TextureResource/9f777a56c7a73fd1782a535dd24430713ce5db932d7c6b7ed9c5d1cd29b88693',
    'TextureResource/8419c3affd4f310ada0d3d5377b5e85c3c3dd5c7effb4696d0cf1b3d362ced42',
    'TextureResource/54fc7e535f380fdc63955077fee0e20cfb991755b9d0e3fa252c2a874cc322de',
    'TextureResource/1376477957fa7d44356bc509ee150b5bad56e3dddb1ac6d455fa06f34d84edf6',
    'TextureResource/5215746fef70499e3cae216b9e2b3e45d7a12778f376046be41f125813edb62d',
    'TextureResource/2b367b608f901105e1e160b5c89de5bcd35218df718a00da4cf6544e25012bc8',
    'TextureResource/c37bca72656a44ef90f87ccbfdb19f5b0d5debd2a2a58c94aad016231e73a0f2',
    'TextureResource/dacaac85e8b85212b930b68f71f30be8c0e205963f1450da96c38d201d6d9ab9',
    'TextureResource/45cfb686af108af582f19d8f4f49d1cacf0364906140fdd43d776441d0b30feb',
    'TextureResource/b1e7caa768ba1156f963df93d6560028a18c861a66bfb34c972cdb7d8fe0fe25',
    'TextureResource/7ed0a474779352421d47486102c090fe572cf737ebff963f91a1eb1e086e2374',
    'TextureResource/59dc2725c4becc5a34abd0042ebff323a1a2e7fc52e2ef7929bcb38a4f5be6cb',
    'TextureResource/b9d18817c96301d68af3b3e94cb453e02f21ec86aeb22cfb58ffed0040bc5919',
    'TextureResource/d11010c82a9e06a4201d3c0f4f8e949a2866104c148f4ca3e85fa1291fb9dfbf',
    'TextureResource/1a52d2f3d4a96db7fa2ea20dcf4c6832ec8ed4ad3908b0b8474ad7bfac229c3b',
    'TextureResource/ed8acd426d35ab81f131db1b92d1928fc60ed71c423129a2b5b8ce550cc38134',
    'TextureResource/25682ef1aa3ba7b55ad02f836191afdfe98b59dfd76e95d6b6e3658f700bf5a6',
    'TextureResource/0a614c91ca9089f083d587d3a42d04f5b231b9a241556b8c5bc8709654d7c6e2',
    'TextureResource/67ad283ac2b1cf93bc2ac2744af281b0223dad8efd58923a786a1a06728fec42',
    'TextureResource/1b3bf62aab051ca643baf748babee3ec5d6c17b64571260f9c4c302051683f95',
    'TextureResource/31a40272f426c6b4cda60b14f01ecc5e1c29b0fa0e688f312230d0c33274a839',
    'TextureResource/eb352a2ca36a37654f51927bc16c187ea11d0f42d8aeebc55b2e90af7907424d',
    'TextureResource/9cd98596f7cd31afe2731ee7cac80e7a4739f3d0953d8986460fbda1e6fa8aa4',
    'TextureResource/f7539a25f029f6f2201a23dc7e477c91832aba0cc778d74bbc0b35dbf013b4cb',
    'TextureResource/039cd2d5d6691a0d55e979fa737c4d613eec9627958007fa14ef3c43633533db',
    'TextureResource/4885bf9f462e8f130cc1fe8321424ad7e1a1b9470ecd74963dd3e01f443ec8e9',
    'TextureResource/588142d3f22a97e210f27db7222dc6b7113864733bb1ca10519b3c1a9386942c',
    'TextureResource/f8e3b071f2bcea6af37213c65abd1d6d4fdae790c965b6b8e7195c722eea78b0',
    'TextureResource/88cf5a3f3568fd915312348bb4697db0c4861b8383cbcdb6f5a9b7c65bd0ca3e',
    'TextureResource/6951dab37bce222b0afa9c9a9cd775c730cd9274368c38b5557960623fff5f1e',
    'TextureResource/4445481ad6e68c3335da3d36f8aab52fc0ee92a73f58b98c70c7951d98d95685',
    'TextureResource/1caf6183bcecaf7988ff6418a81cd96ff5dbe8dbb13fad7027245776362eeef0',
    'TextureResource/9ed7075adc89213c98260c28470a13f987dbae62117f8738ad5934c19a759cca',
    'TextureResource/0e00b26e639395f7aec84e8ff6d405b77eb4a0ea537b6c71ac508bf44afedfa7',
    'TextureResource/a38f5eba6146ff29e7cda0ae929e54a49b0895684df7a79805eef052265d4fea',
    'TextureResource/9987e436fcbf3b507d9bc4a767c22616e29e7e779046f4e9fb91ab4c3a1fc51b',
    'TextureResource/39399e3af4fbe37b177f33304a821485c964f3a29d18c53b7fc633e631715c68',
    'TextureResource/b48d2c32173bf4abb824156b9938fbffa17a8200643d82d5a371c03a519c1320',
    'TextureResource/99300a3eef43ca1fc53a656d34177440a606cd35a5e75e964a709862a1919506',
    'TextureResource/7cc2a4a34fa3c2de33c2db03610603ddb1f2a60a7153dbbc8bab9db400973a88',
    'TextureResource/9717145203c1a8170e020c60b51450204c769badb1f9fd90dc29333c6a10e506',
    'TextureResource/51f683adf0fcf2c8d43c23b9b5196fe7399c92bbf8de1fe96bec96f862487d7a',
    'TextureResource/faa8669b1d1dbdb9c3a6c2d747449da57ce2d70d1934b24479944ca197ce07cd',
    'TextureResource/0066e119a87d65fe222e89a8e7437a33107dce9551c72daad31a55f1d85a2e38',
    'TextureResource/de384ba34369603d820e6521b1be3e78e1c8bf887e174f31f0fe2a092c73bd4d',
    'TextureResource/a410ad26191b2ee2391a0f5946f75bb95ea42b5bc836eb3f787ef21330ef4fe6',
    'TextureResource/087ea4145b9c0511cc1d8cda6103cb3714f0937581ab97eca36ad77a4935f6d6',
    'TextureResource/e6fe828443a594b8e367da54ff802762e13f706b11446f2dd9fc403e3daa7439',
    'TextureResource/ccebadc5af59c7329f62ce49f2c8379997902386757f732cda744821be935efb',
    'TextureResource/d3aa365e3ad5c1f6c1af5fe0113b71741d5671393c777417c6e33c871e28644b',
    'TextureResource/423b7ceefd2956d1ef8b4571a514d21a190184abcbc4ce52d0e5f373b1cab925',
    'TextureResource/e4db35a5a7bb0f01f65bbfc5c56c2ec03fff2f1e325292681e52904e20c01a7c',
    'TextureResource/fa312696cd85afbe1df102dc4b444cb6dc5e22e2ea4c5cfb2121f786c6849715',
    'TextureResource/f6c82679d197eb7cc3dc873d0c3c1df5338c9f0b8094a17074aa95020814c16c',
    'TextureResource/6b76be4cb47b3d58377ec2a97c5e4c36d4bcbd22e78159e9e99fa560d44c9b50',
    'TextureResource/d5e1708ccdc7e7579c1ddd216614a5671a06616e3eeb94e093a844a31e3126b9',
    'TextureResource/c691c4aa803b23e6beaf255f4d61b26cfcca56f4797c4b2a8f8d81b446cf3552',
    'TextureResource/243842328e55ea7d63c674491fc9cfca7ceef6497d814f018473767efeef0b67',
    'TextureResource/dc84ab1a64fce3dbb33dc0029cfeedca8f2c024cedfef29b8694dcf3dbd4edc0',
    'TextureResource/cd0bc9e57ade99e4b34deb23c55352795ce3c8aa74a77c421e1848357d4b3171',
    'TextureResource/fb7b529d09535f98eb7c222a067803b342a4fc81dfadef8327da56871d5518b8',
    'TextureResource/777e94207c5093e30735aaa2e1c6c8579d618f1001c6628a40ba82a76e97f1c4',
    'TextureResource/64bab00df5b9f43d32e4284ce0b9b31056c7c956b5ef9ee57e77c2495457fcd8',
    'TextureResource/61c5c76712dbb46094c1c72baadc37454ff614673a3276558e7e9f9568ceb3a1',
    'TextureResource/7b031b6c82084f7a1655681208b7f2dd024e4370739d3f17424744a5d4b12fd3',
    'TextureResource/fb2a08cb2f7b555c99b5b04644218a05a55feee3f5de0b8f2d2f370b7a89066a',
    'TextureResource/dc764ac8e679c7c5be95d0bb4a224b013c959c10a896c934863e4fecb7381f10',
    'TextureResource/99313ac8f785dd3b5a87e8e8a20e71585fba4e59817f33fc287db236e205a768',
    'TextureResource/14f731fb2b0132e906fb9e5ee067c192dcf1c9b9d826708737413e3d06a5f5fe',
    'TextureResource/cda64191bf6cffb1f52e4263ba39850d9e109ff0fd201b762cfbe55005aeea02',
    'TextureResource/80ac97439bcf75c29f50b905cda9349c71e93c423b8e77772df6fafafd223c03',
    'TextureResource/d25b615eb75827f9c59b06372f08a1da3133ec0ddaae07f3a999f3974115cfc0'
]

another_possible_data_spider: list[str] = [
    'TextureResource/7629c99738bd304814e595ad5fdadd0a02c0b91f9cf8eff4cdf0c2976a1fb203',
    'TextureResource/2126464d2babe9f06beeebb6a63cc778e7aa6eed4eba144365ed75db8c2d75a4',
    'TextureResource/cc05618627ebd3adefcf1aed645b00d8b2f6712dc937fa88ff6bc72b3974c48d',
    'TextureResource/d88119b0a1cf95e232e683bc5961419b1a937753bd4350a1030204f9ae84de34',
    'TextureResource/a3f6919d78e4ddaf3d42bf19e6cbc16789f1cd85cc597ffa7cb290684ee48f70',
    'TextureResource/8419c3affd4f310ada0d3d5377b5e85c3c3dd5c7effb4696d0cf1b3d362ced42',
    'TextureResource/039cd2d5d6691a0d55e979fa737c4d613eec9627958007fa14ef3c43633533db',
    'TextureResource/f8e3b071f2bcea6af37213c65abd1d6d4fdae790c965b6b8e7195c722eea78b0',
    'TextureResource/6951dab37bce222b0afa9c9a9cd775c730cd9274368c38b5557960623fff5f1e',
    'TextureResource/e6fe828443a594b8e367da54ff802762e13f706b11446f2dd9fc403e3daa7439',
    'TextureResource/64bab00df5b9f43d32e4284ce0b9b31056c7c956b5ef9ee57e77c2495457fcd8',
    'TextureResource/14f731fb2b0132e906fb9e5ee067c192dcf1c9b9d826708737413e3d06a5f5fe'
]

ROOT_PATH: str = os.path.dirname(os.path.abspath(__file__))

map_data: str = open(
    os.path.join(ROOT_PATH, 'map_data.txt'), 'r'
).read()


map_data_textures: list[str] = [
    texture for texture in map_data.splitlines()
    if 'TextureResource/' in texture and texture != 'TextureResource/'
]


contains_count: int = 0

for texture in map_data_textures:
    if texture in possible_spider_textures:
        contains_count += 1
        print(
            f'"{texture}" TEXTURE CONTAINS IN POSSIBLE SPIDER TEXTURES BY BIG CONTENT'
        )

percentage: float = contains_count / len(possible_spider_textures) * 100
print()
print(f'PERCENTAGE OF CONTAINED VALUE => "{percentage}"')
print(
    'MIGHT BE FOUND BY BIG CONTENT' if percentage > 90 else 'LOOKS LIKE NOT FOUND BY BIG CONTENT'
)
print()
print('*'*50)
print()
contains_count: int = 0

for texture in map_data_textures:
    if texture in another_possible_data_spider:
        contains_count += 1
        print(
            f'"{texture}" TEXTURE CONTAINS IN POSSIBLE SPIDER TEXTURES BY LITTLE CONTENT'
        )

percentage: float = contains_count / len(another_possible_data_spider) * 100

print()
print(f'PERCENTAGE OF CONTAINED VALUE => "{percentage}" BY LITTLE CONTENT')
print(
    'MIGHT BE FOUND BY LITTLE CONTENT' if percentage > 50 else 'LOOKS LIKE NOT FOUND BY LITTLE CONTENT'
)
print()

print(
    'TextureResource/9987e436fcbf3b507d9bc4a767c22616e29e7e779046f4e9fb91ab4c3a1fc51b' in map_data_textures
    or 'TextureResource/37c17b35bc692babd72f7edeb72aff699a18be39b91350791acced9fdbda38e1' in map_data_textures
    or 'TextureResource/37c17b35bc692babd72f7edeb72aff699a18be39b91350791acced9fdbda38e1' in map_data_textures
)
