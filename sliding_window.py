
rules = {"user1":{"requests_num": "10", "time_window":"1"}}

def get_rules(user):
    return rules.get(user)

def get_map():
    pass

def allow(self):
    pass

if __name__ == '__main__':
    rules = get_rules('user1')
    print(rules)


    