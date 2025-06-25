from .base_page import BasePage
from .locators import BasketPageLocators as Locators

class Languages:

    languages_all = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "en-gb": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }

class BasketPage(BasePage):

    def should_not_be_products_in_the_basket(self):
        assert self.is_not_element_present(*Locators.BASKET_ITEMS), "Basket is not empty"

    def should_be_message_that_basket_is_empty(self):
        current_language = self.current_language()
        message_basket = self.find_element_ex_wait(*Locators.BASKET_MESSAGE).text
        assert Languages.languages_all[current_language] in message_basket, "'Basket message' is not correct"
