import os
import yaml


def write(new_yaml_data_dict,data_name):

    if not os.path.isfile("data/{0}.yaml".format(data_name)):

        with open("data/{0}.yaml".format(data_name), "a") as fo:
            fo.write("---\n")

    sdump = yaml.dump(
                new_yaml_data_dict
                )

    with open("data/{0}.yaml".format(data_name), "a") as fo:
        fo.write(sdump)


def user(user_data):
    with open("user.yaml", "w") as fo:
        fo.write(yaml.dump(user_data))


def get_user():
    with open("user.yaml", "r") as fo:
        documents = yaml.full_load(fo)
        return documents



def print_yaml(data_name):

    with open(r'data/{0}.yaml'.format(data_name)) as file:
        documents = yaml.full_load(file)

        for item, doc in documents.items():
            print(item, " - ", data_name, " ",  doc.get(data_name))

def get_yaml_sorted(data_name):

    with open(r'data/{0}.yaml'.format(data_name)) as file:
        documents = yaml.full_load(file)
        sort_file = yaml.dump(documents, sort_keys=True)
        print(sort_file)

def get_yaml(data_name):

    with open(r'data/{0}.yaml'.format(data_name)) as file:
        documents = yaml.full_load(file)
    return documents


def test():
    new_yaml_data_dict = {
            '2018-01-20': {
                'weight': 66,
            }
        }
    write(new_yaml_data_dict,'weight')

    new_yaml_data_dict = {
            '2018-02-20': {
                'weight': 69,
                'comment': 'to jest est'
            }
        }

    write(new_yaml_data_dict,'weight')

    new_yaml_data_dict = {
            '2018-01-20': {
                'height': 166,
            }
        }
    write(new_yaml_data_dict,'height')

    new_yaml_data_dict = {
            '2018-02-20': {
                'height': 169,
                'comment': 'to jest est'
            }
        }

    write(new_yaml_data_dict,'height')


    get_yaml('weight')
    get_yaml('height')
    print_yaml('weight')
    print_yaml('height')
    get_yaml_sorted('weight')
    get_yaml_sorted('height')


dic = get_yaml('weight')
print(dic)
sort_orders = sorted(dic.items(), key=lambda x: x[0], reverse=False)
print(sort_orders)

