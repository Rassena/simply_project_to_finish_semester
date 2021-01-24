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
