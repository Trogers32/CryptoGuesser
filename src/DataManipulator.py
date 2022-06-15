import csv
from models.PostData import PostData


# Primitive relevancy determination just counting mentions
def determine_relevancy(crypto_postings):
    rankings = {}

    for reddit_post in crypto_postings:
        title = reddit_post.get('title')
        for c in crypto:
            if c in title:
                if c not in rankings:
                    rankings[c] = PostData(c, 1, reddit_post.get('created_on'))
                else:
                    rankings[c].mentions += 1

    rank_list = list(rankings.values())
    sorted_rank_list = sorted(rank_list, key=lambda cr: cr.mentions, reverse=True)
    for x in sorted_rank_list:
        print(f"{x.crypto_mentioned} - {x.mentions} - {x.created_on}")

    return sorted_rank_list


def write_to_file(data):
    f = open('../RedditPosts.csv', 'w')
    writer = csv.writer(f)

    for content in data:
        writer.writerow([content.crypto_mentioned, content.mentions, content.created_on])

    f.close()


crypto = [
    'BTC', 'ETH', 'USDT', 'BNB', 'USDC', 'XRP', 'SOL', 'ADA', 'LUNA', 'AVAX', 'DOGE', 'DOT', 'BUSD', 'UST', 'SHIB',
    'WBTC', 'NEAR', 'MATIC', 'CRO', 'DAI', 'LTC', 'ATOM', 'UNI', 'BCH', 'LINK', 'TRX', 'FTT', 'LEO', 'XLM', 'ETC',
    'ALGO', 'XMR', 'VET', 'MANA', 'HBAR', 'ICP', 'FIL', 'APE', 'EGLD', 'SAND', 'THETA', 'FTM', 'AXS', 'XTZ', 'RUNE',
    'KLAY', 'AAVE', 'HNT', 'EOS', 'WAVES', 'CAKE', 'FLOW', 'ZEC', 'MKR', 'MIOTA', 'BTT', 'XEC', 'GRT', 'CVX', 'BSV',
    'KCS', 'STX', 'NEO', 'HT', 'ONE', 'CHZ', 'ZIL', 'GALA', 'QNT', 'KSM', 'CELO', 'TUSD', 'NEXO', 'ENJ', 'GMT', 'LRC',
    'OKB', 'DASH', 'BAT', 'MINA', 'CRV', 'AR', 'USDN', 'COMP', 'KDA', 'AMP', 'USDP', 'GLMR', 'XEM', 'TFUEL', 'HOT',
    'ROSE', 'SCRT', 'KNC', 'DCR', 'KAVA', 'AUDIO', 'ANC', 'IOTX', 'BORA', 'ICX', 'QTUM', 'YFI', 'SKL', 'OMG', 'XDC',
    'XYM', 'GNO', 'ZRX', '1INCH', 'PAXG', 'ANKR', 'SNX', 'BTG', 'SXP', 'BNT', 'RVN', 'JST', 'IOST', 'WAXP', 'ACA',
    'SC', 'GT', 'LPT', 'CEL', 'VLX', 'WOO', 'RNDR', 'RENBTC', 'FXS', 'ZEN', 'CHSB', 'NFT', 'RLY', 'BRG', 'ONT', 'ELON',
    'GLM', 'IMX', 'STORJ', 'UMA', 'FEI', 'SUSHI', 'VGX', 'REV', 'DGB', 'HIVE', 'POLY', 'CEEK', 'TEL', 'KEEP', 'CSPR',
    'SPELL', 'CELR', 'ILV', 'XDB', 'BTRST', 'PLA', 'FLUX', 'SYS', 'REN', 'SRM', 'CKB', 'TWT', 'DYDX', 'OCEAN', 'PERP',
    'PYR', 'C98', 'UOS', 'XNO', 'ENS', 'WIN', 'MXC', 'DENT', 'LSK', 'CFX', 'COTI', 'NU', 'XPRT', 'PEOPLE', 'RAY',
    'JOE', 'INJ', 'SUPER', 'TRIBE', 'POWR', 'FET', 'YGG', 'MED', 'CHR', 'MX', 'SNT', 'WRX', 'MBOX', 'XCH', 'XYO',
    'BOBA', 'REQ', 'MOVR', 'Bitcoin', 'Ethereum', 'Tether', 'BNB', 'USD Coin', 'XRP', 'Solana', 'Cardano', 'Terra',
    'Polkadot', 'Binance USD', 'TerraUSD', 'Shiba Inu', 'Wrapped Bitcoin', 'NEAR Protocol', 'Polygon', 'Cronos', 'Dai',
    'Litecoin', 'Cosmos', 'Uniswap', 'Bitcoin Cash', 'Chainlink', 'TRON', 'FTX Token', 'UNUS SED LEO', 'Stellar',
    'Ethereum Classic', 'Algorand', 'Monero', 'VeChain', 'Decentraland', 'Hedera', 'Internet Computer', 'Filecoin',
    'ApeCoin', 'Elrond', 'The Sandbox', 'Theta Network', 'Fantom', 'Axie Infinity', 'Tezos', 'THORChain', 'Klaytn',
    'Aave', 'Helium', 'EOS', 'Waves', 'PancakeSwap', 'Flow', 'Zcash', 'Maker', 'IOTA', 'BitTorrent-New', 'eCash',
    'The Graph', 'Convex Finance', 'Bitcoin SV', 'KuCoin Token', 'Stacks', 'Neo', 'Huobi Token', 'Harmony', 'Chiliz',
    'Zilliqa', 'Gala', 'Quant', 'Kusama', 'Celo', 'TrueUSD', 'Nexo', 'Enjin Coin', 'STEPN', 'Loopring', 'OKB', 'Dash',
    'Basic Attention Token', 'Mina', 'Curve DAO Token', 'Arweave', 'Neutrino USD', 'Compound', 'Kadena', 'Amp',
    'Pax Dollar', 'Moonbeam', 'NEM', 'Theta Fuel', 'Holo', 'Oasis Network', 'Secret', 'Kyber Network Crystal v2',
    'Decred', 'Kava', 'Audius', 'Anchor Protocol', 'IoTeX', 'BORA', 'ICON', 'Qtum', 'yearn.finance', 'SKALE Network',
    'OMG Network', 'XDC Network', 'Symbol', 'Gnosis', '0x', '1inch Network', 'PAX Gold', 'Ankr', 'Synthetix',
    'Bitcoin Gold', 'SXP', 'Bancor', 'Ravencoin', 'JUST', 'IOST', 'WAX', 'Acala Token', 'Siacoin', 'GateToken',
    'Livepeer', 'Celsius', 'Velas', 'WOO Network', 'Render Token', 'renBTC', 'Frax Share', 'Horizen', 'SwissBorg',
    'APENFT', 'Rally', 'Bridge Oracle', 'Ontology', 'Dogelon Mars', 'Golem', 'Immutable X', 'Storj', 'UMA', 'Fei USD',
    'SushiSwap', 'Voyager Token', 'Revain', 'DigiByte', 'Hive', 'Polymath', 'CEEK VR', 'Telcoin', 'Keep Network',
    'Casper', 'Spell Token', 'Celer Network', 'Illuvium', 'DigitalBits', 'Braintrust', 'PlayDapp', 'Flux', 'Syscoin',
    'Ren', 'Serum', 'Nervos Network', 'Trust Wallet Token', 'dYdX', 'Ocean Protocol', 'Perpetual Protocol',
    'Vulcan Forged PYR', 'Coin98', 'Ultra', 'Nano', 'Ethereum Name Service', 'WINkLink', 'MXC', 'Dent', 'Lisk',
    'Conflux', 'COTI', 'NuCypher', 'Persistence', 'ConstitutionDAO', 'Raydium', 'JOE', 'Injective', 'SuperFarm',
    'Tribe', 'Powerledger', 'Fetch.ai', 'Yield Guild Games', 'MediBloc', 'Chromia', 'MX TOKEN', 'Status', 'WazirX',
    'MOBOX', 'Chia', 'XYO', 'Boba Network', 'Request', 'Moonriver', 'Avalanche', 'Dogecoin'
]
