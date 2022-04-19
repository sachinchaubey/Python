import instaloader

mod = instaloader.Instaloader()
inpu = input("Enter user name: ")
mod.download_profile(inpu,profile_pic_only = True)