import argparse
import pandas as pd
from core_extract_comments import *
from core_utils import *
#from TkinterTest import *
start = time.time()

def run(search, input_product_ids_filename,cons):
    if input_product_ids_filename is not None:
        with open(input_product_ids_filename, 'r') as r:
            product_ids1 = [p.strip() for p in r.readlines()]
            logging.info('{} product ids were found.'.format(len(product_ids1)))
            reviews_counter = 0
            for product_id in product_ids1:
                _, exist = get_reviews_filename(product_id)
                if exist:
                    logging.info('product id [{}] was already fetched. Skipping.'.format(product_id))
                    continue
                reviews = get_comments_with_product_id(product_id)
                reviews_counter += len(reviews)
                logging.info('{} reviews found so far.'.format(reviews_counter))
                persist_comment_to_disk(reviews)
    else:
        default_search = cons
        #default_search = 'Milton Pinnacle 1900 Insulated Thermosteel, 1.9 ml (Silver)'
        print(cons)
        search = default_search if search is None else search
        print(search)
        reviews1 = get_comments_based_on_keyword(search)
        #persist_comment_to_disk(str(reviews))
        return reviews1


def get_script_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--search')
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    input_product_ids_filename = args.input
    search = args.search
    return search, input_product_ids_filename


def main(cons):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    search, input_product_ids_filename = get_script_arguments()
    e = run(search, input_product_ids_filename,cons)
    driver.close()
    driver.quit()
    C = []
    for product_id in e:
        #output_filename, exist = get_reviews_filename(product_id)
        C.append(pd.read_csv(product_id, encoding='utf-8-sig'))
    return [i.head() for i in C]

'''
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
    ASIN = 'B07NYZZ28B'
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    output_filename1, exist = get_reviews_filename(ASIN)
    if exist:
        print("File with same pid is there....")

    else:
        _reviews = get_comments_with_product_id(ASIN)
        persist_comment_to_disk(_reviews)
'''

#driver.close()
#driver.quit()

stop = time.time()
print("elapsed time is:",str(stop-start)+"s")