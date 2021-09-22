import cv2


def commons(checker: str):

    checker = f'configs/images/{checker}'
    checkeie = 'configs/images/screenshot.png'
    img_screen = cv2.imread(checkeie)
    img_gray = cv2.cvtColor(img_screen, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(checker)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    return result


def couter(photo, threshold: float = 0.9):
    places = []
    for commons_line in commons(photo):
        for i in commons_line:
            if i >= threshold:
                places.append(i)
    return places
