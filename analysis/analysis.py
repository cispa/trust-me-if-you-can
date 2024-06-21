from collections import defaultdict
import tldextract
import itertools
import psycopg2
import json
import os

SHOW_DOMAINS = False

db_conf = os.environ.get('DBCONF', None)
conn = psycopg2.connect(db_conf)
cur = conn.cursor()

TLD_CACHE = dict()


def get_site(origin):
    if origin in TLD_CACHE:
        return TLD_CACHE[origin]
    e = tldextract.extract(origin)
    TLD_CACHE[origin] = e.registered_domain
    return e.registered_domain


def analytics(platforms):
    out_sites = defaultdict(set)
    out_domains = defaultdict(set)
    for p, url in platforms.items():
        cur.execute(f"SELECT DISTINCT domain FROM inclusions WHERE script LIKE '{url}';")
        for origin in cur.fetchall():
            e = tldextract.extract(origin[0])
            out_domains[p].add('.'.join(e))
            out_sites[p].add(e.registered_domain)

    print('==> Sites:')
    print('====> Single Platforms:')
    all_inter_site = set(out_sites['twitter'])
    for p in platforms.keys():
        print(f'{p}: {len(out_sites[p])}')
        all_inter_site = all_inter_site.intersection(out_sites[p])
    print('====> Intersections:')
    for p1, p2 in list(itertools.combinations(platforms.keys(), 2)):
        print(f'Inter_{p1}_{p2}: {len(out_sites[p1].intersection(out_sites[p2]))}')
    print('====> ALL:')
    print('ALL:', len(all_inter_site))
    print()

    if SHOW_DOMAINS:
        print('==> Domains:')
        print('====> Single Platforms:')
        all_inter_dom = set(out_domains['twitter'])
        for p in platforms.keys():
            print(f'{p}: {len(out_domains[p])}')
            all_inter_dom = all_inter_dom.intersection(out_domains[p])
        print('====> Intersections:')
        for p1, p2 in list(itertools.combinations(platforms.keys(), 2)):
            print(f'Inter_{p1}_{p2}: {len(out_domains[p1].intersection(out_domains[p2]))}')
        print('====> ALL:')
        print('ALL:', len(all_inter_dom))
        print()


def frequency():
    data = defaultdict(set)
    cur.execute(f"SELECT script, domain FROM inclusions;")
    for script, origin in cur.fetchall():
        data[get_site(script)].add(get_site(origin))
    out = list()
    for script_src, loaded_sites in data.items():
        out.append([script_src, len(loaded_sites)])
    return dict(sorted(out, key=lambda t: t[1], reverse=True))


def main():
    json.dump(frequency(), open('most_loaded_resources.json', 'w'))

    print('Social Platforms')
    social_platforms = {
        'facebook': 'http%://connect.facebook.net/%/sdk.js%',
        'twitter': 'http%://platform.twitter.com/widgets.js%',
        'pinterest': 'http%://assets.pinterest.com/js/pinit.js%',
        'youtube': 'http%://apis.google.com/js/platform.js%'
    }
    analytics(social_platforms)

    print('Analytics Services')
    analytics_platforms = {
        'google': 'https://www.google-analytics.com/analytics.js%',
        'newrelic': 'http%://js-agent.newrelic.com/nr%.js%',
        'scorecard': 'http%://sb.scorecardresearch.com/beacon.js',
        'adobetm': 'http%://assets.adobedtm.com/%'
    }
    analytics(analytics_platforms)

    print('Maps integration')
    discussion_platforms = {
        'osm': 'http%//www.openlayers.org/api/OpenLayers.js%',
        'google': 'http%://maps.googleapis.com/maps/api/%',
        'bing': 'http%://www.bing.com/api/maps/%',
    }
    analytics(discussion_platforms)

    print('Frameworks:')
    frameworks = {
        'jquery': '%/jquery%',
        'bootstrap': '%/bootstrap%',
        'angular': '%/angular%',
        'dojo': '%/dojo%',
        'backbone': '%/backbone%',
        'vue': '%/vue%',
        'ember': '%/ember%',
    }
    analytics(frameworks)

    print('Discussion Plugins:')
    discussion_platforms = {
        'disquis': '%disqus.com/embed.js%',
    }
    analytics(discussion_platforms)


if __name__ == '__main__':
    main()
