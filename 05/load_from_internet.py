from threading import Thread
import urllib.request
import uuid


list_of_images = ['https://i.allo.ua/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/i/p'
                  '/iphone_11_pro_sg_2_3.jpg',
                  'https://i.citrus.ua/imgcache/size_800/uploads/shop/5/5/5533198c217ea9a4280fdf804df8f088.jpg',
                  'https://i.citrus.ua/uploads/shop/a/f/af1494a53269360c3e4b9a6f6d596b9f.jpg',
                  'https://i.citrus.ua/uploads/shop/8/d/8de88b21a5fe0f39a08f46d83f18f884.jpg',
                  'https://i.citrus.ua/uploads/shop/c/4/c4d055c57b546cc70e961480a1cf1fcc.jpg',
                  'https://i.citrus.ua/uploads/shop/d/5/d5c52766f9daec1ea3517cbde9e99f3d.jpg',
                  'https://i.citrus.ua/uploads/shop/2/d/2d2e1dcdbd18270228e46d633814ab33.jpg',
                  'https://i.citrus.ua/uploads/shop/4/1/41900d6e9109eead5603eb3adadc6a8e.jpg',
                  'https://i.citrus.ua/uploads/shop/e/f/ef6b0fa5318402909290f62ef4c8b297.jpg',
                  'https://i.citrus.ua/uploads/shop/4/1/41741c9536e0f07fa3e675e9c7b18091.jpg']


def my_decorator(link_list):

    def wrapper(func):

        thread_list = []

        for link in link_list:

            t = Thread(target=func, args=(link, ))
            thread_list.append(t)
            t.start()
            print(f'Thread \'{t.getName()}\' for URL: \'{link}\' was Started')

        while len(thread_list) > 0:
            for thread in thread_list:
                if not thread.is_alive():
                    thread_list.remove(thread)
                    print(f'Thread \'{thread.getName()}\' was Completed')

    return wrapper


@my_decorator(list_of_images)
def load_image(link):
    urllib.request.urlretrieve(link, str(uuid.uuid4().hex + '.jpg'))


here_we_load_everything = load_image
