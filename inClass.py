class Phone:
    def __init__(self, phoneName, storageLimit, isAndroid, screenSize, hasHeadPhoneJack):
        self.name = phoneName
        self.limit = storageLimit
        self.android = isAndroid
        self.size = screenSize
        self.headphone = hasHeadPhoneJack

    def print_props(self):
        print(
            f"The phone {self.name} has {self.limit} of space and a {self.size} screen.\nAndroid: {self.android}\nDoes it have a headphone jack: {self.headphone}")

    def __str__(self):
        my_instance_string = f"Properties for the phone:\n" \
                             f"name = {self.name}\n" \
                             f"limit = {self.limit}\n" \
                             f"android = {self.android}\n" \
                             f"size = {self.size}\n" \
                             f"headphone = {self.headphone}"
        return my_instance_string


iphone = Phone("iPhone", "64GB", "No", "3 inch", "Yes")
print(iphone)
# iphone.print_props()
#
#
# class TwitterUser:
#     def __init__(self, userName, followingNumber, followersNumber, pictureURL):
#         self.name = userName
#         self.following = followingNumber
#         self.follower = followersNumber
#         self.pic = pictureURL
#
#
# newUser = TwitterUser("Andrew", "90", "95", "VeryHandsome.jpeg")
# print(newUser.name, newUser.follower, newUser.following, newUser.pic)
#
#
# class GitHubRepository:
#     def __init__(self, userName, fileName, descriptionOfRepository, code):
#         self.name = userName
#         self.file = fileName
#         self.description = descriptionOfRepository
#         self.code = code
#
# newRepository = GitHubRepository("atdaunais","goodfile","Repositroy descrip","Here's that lovely code")
# print(f"{newRepository.name}\n{newRepository.file}\n{newRepository.description}\n{newRepository.code}")
