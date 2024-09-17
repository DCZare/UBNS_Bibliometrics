def city_lookup():

    filter_str = 'authorships.institutions.lineage:i4210157890,publication_year:%3E2023'

    email = "davidzar@buffalo.edu"

    endpoint = 'works'

    filters = ",".join((
        f'{filter_str}',
    ))

    filtered_works_url = f'https://api.openalex.org/{endpoint}?filter={filters}'
    if email:
        filtered_works_url += f"&mailto={email}"
    print(f'complete URL with filters:\n{filtered_works_url}')

    import requests

    import pandas as pd

    cursor = '*'

    select = ",".join((
        'id',
        'ids',
        'title',
        'display_name',
        'publication_year',
        'publication_date',
        'primary_location',
        'open_access',
        'authorships',
        'cited_by_count',
        'is_retracted',
        'is_paratext',
        'updated_date',
        'created_date',
    ))


    works = []
    loop_index = 0
    while cursor:
        
        url = f'{filtered_works_url}&select={select}&cursor={cursor}'
        page_with_results = requests.get(url).json()
        
        results = page_with_results['results']
        works.extend(results)

        cursor = page_with_results['meta']['next_cursor']
        loop_index += 1
        if loop_index in [5, 10, 20, 50, 100] or loop_index % 500 == 0:
            print(f'{loop_index} api requests made so far')
    print(f'done. made {loop_index} api requests. collected {len(works)} works')

    data = []
    for work in works:
        for authorship in work['authorships']:
            if authorship:
                author = authorship['author']
                author_id = author['id'] if author else None
                author_name = author['display_name'] if author else None
                author_position = authorship['author_position']
                for institution in authorship['institutions']:
                    if institution:
                        institution_id = institution['id']
                        institution_name = institution['display_name']
                        institution_country_code = institution['country_code']
                        data.append({
                            'work_id': work['id'],
                            'work_title': work['title'],
                            'work_display_name': work['display_name'],
                            'work_publication_year': work['publication_year'],
                            'work_publication_date': work['publication_date'],
                            'author_id': author_id,
                            'author_name': author_name,
                            'author_position': author_position,
                            'institution_id': institution_id,
                            'institution_name': institution_name,
                            'institution_country_code': institution_country_code,
                        })
    df = pd.DataFrame(data)

    institution_ids = df['institution_id'].dropna().unique()

    
    endpoint = "institutions"
    size = 50
    loop_index = 0
    institutions = []
    for list_index in range(0, len(institution_ids), size):
        subset = institution_ids[list_index:list_index+size]
        pipe_separated_ids = "|".join(subset)
        r = requests.get(f"https://api.openalex.org/institutions?filter=openalex:{pipe_separated_ids}&per-page={size}")
        results = r.json()['results']
        institutions.extend(results)
        loop_index += 1
    print(f"collected {len(institutions)} institutions using {loop_index} api calls")

    data = []
    for institution in institutions:
        data.append({
            'display_name': institution['display_name'],
            'id': institution['id'],
            'city': institution['geo']['city'],
        })

    df_institutions = pd.DataFrame(data)

    outpath = 'build/data/city_match_out.csv'
    df_institutions.to_csv(outpath, index=False)

    print('--------------------------------')
    print('City Matching Completed.')
    print('CSV Generated.')
    print('--------------------------------')

city_lookup()

