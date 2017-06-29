# Практическая работа №2
Создание на языке программирования Python (v 3.6.1) двух программ, посылающих друг другу данные через сокеты UDP:

*Клиент формирует пакет UDP по определённому принципу и отправляет его на сервер.

*Сервер принимает пакет UDP, проводит над ним действие и отправляет обратно, попутно печатает, от кого пришёл пакет (IP-адрес клиента)

*Клиент принимает пакет UDP и печатает его содержимое, а также IP-адрес сервера

При запуске обеих программ клиент получает адрес сервера, и готовится принимать udp с любых адресов (не только перечисленных в ipconfig данной системы, т.е.) через порт УКАЗАННЫЙ_В_recf = ('', 11101), и готовится отсылать сообщения на УКАЗАННЫЙ_В_send_to = (server, 11100) порт сервера. 
Соответственно, для этого создаются два сокета, один из которых(принимающий) биндит порт recf = ('', 11101), т.е. ассоциирует себя с ним для дальнейшей работы.
Далее в бесконечном цикле идет ввод и кодирование в utf-8 сообщения, а после отправка средствами ранее отведенного для этого сокета. 
После же идет ожидание ответа от сервера, который после и выводится вместе с временем прибытия ответа клиенту.
Сервер же отличается от клиента лишь наличием у него функции-обработчика входящих сообщений, поменянными местами портами приема себе и передачи клиенту, и частично переделанным (под постоянное ожидание без ввода) бесконечным циклом и выводом.
