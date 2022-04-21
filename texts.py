from aiogram.utils.markdown import link, text, code, hcode, hlink


def ant_text(ant):
    return text(f'🐜{ant.name}🐜',
                f'\n{ant.description}')


def ls_text(login, all_buys, balance):
    ls_text = text('➖➖➖➖➖➖➖➖➖➖➖',
                   '\nℹ️ Информация о вас:',
                   '\n🔑 Логин: @', login,
                   '\n💵 Покупок на сумму: ', hcode(all_buys), ' ₽',
                   '\n🏦 Баланс: ', hcode(balance), ' ₽',
                   '\n➖➖➖➖➖➖➖➖➖➖➖', sep='')
    return ls_text


def pay_text(pay_url, balance):
    pay_text = text(f'Пополнение на сумму:', code(f'{balance}₽'),
                    f'\nОпатите в течение', code('5'), 'минут⏱',
                    link('\nНажите, чтобы оплатить', pay_url))

    return pay_text


info_text = 'Муравьи это сельскохозяйственные работники микромира. В их крохотной головке примерно 250 000 клеток ' \
            'мозга, они самые умные, сильные и изобретательные насекомые. Чтобы познакомить ребенка с удивительным ' \
            'миром этих маленьких насекомых, можно заказать муравьиную ферму - закрытый муравейник для наблюдения за ' \
            'муравьями. '

help_text = 'Поможет разобраться во всем @ivan_mironov83638'
