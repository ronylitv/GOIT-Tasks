from setuptools import setup

slovar = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}



def do_setup(args_dict):
    setup_list = []
    for ind, val in args_dict.items():
        setup_list.append(val)
    setup(
        name=setup_list[0],
        version=setup_list[1],
        description=setup_list[2],
        url=setup_list[3],
        author=setup_list[4],
        author_email=setup_list[5],
        license=setup_list[6],
        packages=setup_list[7]

    )

do_setup(slovar)











