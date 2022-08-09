class UserData:
    emails = [
        'michael.lawson@reqres.in',
        'lindsay.ferguson@reqres.in',
        'tobias.funke@reqres.in',
        'byron.fields@reqres.in',
        'rachel.howell@reqres.in',
        'george.edwards@reqres.in'
    ]
    first_names = [
        'Michael',
        'Lindsay',
        'Tobias',
        'Byron',
        'George',
        'Rachel'
    ]
    last_names = [
        'Lawson',
        'Ferguson',
        'Funke',
        'Fields',
        'Edwards',
        'Howell'
    ]
    avatars = [
        "https://reqres.in/img/faces/7-image.jpg",
        "https://reqres.in/img/faces/8-image.jpg",
        "https://reqres.in/img/faces/9-image.jpg",
        "https://reqres.in/img/faces/10-image.jpg",
        "https://reqres.in/img/faces/11-image.jpg",
        "https://reqres.in/img/faces/12-image.jpg"
    ]


class CreatedUser:
    user_name_job = {
        'name': 'Antoine Ivashchuk',
        'job': 'French teacher',
    }
    updated_job = {
        'job': 'French interpreter'
    }
    updated_user_name_job = {
        'name': 'Antoine Ivashchuk',
        'job': 'French teacher',
    }


class DeletedUser:
    deleted_user_data = {
        'id': 2,
        'email': 'janet.weaver@reqres.in',
        'first_name': 'Janet',
        'last_name': 'Weaver',
        'avatar': 'https://reqres.in/img/faces/2-image.jpg'
    }


class RegisterUser:
    register_successful_data = {
        'id': 4,
        'token': 'QpwL5tke4Pnpja7X4'
    }
    register_unsuccessful_data = {
        "error": "Missing password"
    }
