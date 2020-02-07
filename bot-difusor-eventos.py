#Libreria
import telebot, os, telegram, time
from telebot import types
import datetime
import telebot_calendar
from telebot_calendar import CallbackData
from telebot.types import ReplyKeyboardRemove, CallbackQuery

################################# GLOBAL VARS #######################################3
token = '' #poner api:key
bot = telebot.TeleBot(token)
send_to = "" # id del user, -100(id del canal privado) o canal con @nombre , que recibira la alerta


DESCRIPCION = "Bienvenido para crear una nueva alerta escribe el comando /new y sigue las instrucciones .."

############ MENU ############

#declaraciones
start_markup = types.InlineKeyboardMarkup()
clock_markup = types.InlineKeyboardMarkup()
mult_markup = types.InlineKeyboardMarkup()
bool_markup_send = types.InlineKeyboardMarkup()

#buttons
opt1_button = types.InlineKeyboardButton("Concierto", callback_data="concierto")
opt2_button = types.InlineKeyboardButton("Charla",callback_data="charla")
opt3_button = types.InlineKeyboardButton("Espectaculo",callback_data="espectaculo")

photo_button = types.InlineKeyboardButton('Photo\n', callback_data='mult_photo')
video_button = types.InlineKeyboardButton('Video\n', callback_data='mult_video')
no_button = types.InlineKeyboardButton('No\n', callback_data='mult_no')
si_button_send = types.InlineKeyboardButton('Si\n', callback_data='send_si')
no_button_send = types.InlineKeyboardButton('No\n', callback_data='send_no')
clock_now = types.InlineKeyboardButton('Actual\n', callback_data='hora_actual')
clock_00 = types.InlineKeyboardButton('00:00\n', callback_data='hora_00')
clock_01 = types.InlineKeyboardButton('01:00\n', callback_data='hora_01')
clock_02 = types.InlineKeyboardButton('02:00\n', callback_data='hora_02')
clock_03 = types.InlineKeyboardButton('03:00\n', callback_data='hora_03')
clock_04 = types.InlineKeyboardButton('04:00\n', callback_data='hora_04')
clock_05 = types.InlineKeyboardButton('05:00\n', callback_data='hora_05')
clock_06 = types.InlineKeyboardButton('06:00\n', callback_data='hora_06')
clock_07 = types.InlineKeyboardButton('07:00\n', callback_data='hora_07')
clock_08 = types.InlineKeyboardButton('08:00\n', callback_data='hora_08')
clock_09 = types.InlineKeyboardButton('09:00\n', callback_data='hora_09')
clock_10 = types.InlineKeyboardButton('10:00\n', callback_data='hora_10')
clock_11 = types.InlineKeyboardButton('11:00\n', callback_data='hora_11')
clock_12 = types.InlineKeyboardButton('12:00\n', callback_data='hora_12')
clock_13 = types.InlineKeyboardButton('13:00\n', callback_data='hora_13')
clock_14 = types.InlineKeyboardButton('14:00\n', callback_data='hora_14')
clock_15 = types.InlineKeyboardButton('15:00\n', callback_data='hora_15')
clock_16 = types.InlineKeyboardButton('16:00\n', callback_data='hora_16')
clock_17 = types.InlineKeyboardButton('17:00\n', callback_data='hora_17')
clock_18 = types.InlineKeyboardButton('18:00\n', callback_data='hora_18')
clock_19 = types.InlineKeyboardButton('19:00\n', callback_data='hora_19')
clock_20 = types.InlineKeyboardButton('20:00\n', callback_data='hora_20')
clock_21 = types.InlineKeyboardButton('21:00\n', callback_data='hora_21')
clock_22 = types.InlineKeyboardButton('22:00\n', callback_data='hora_22')
clock_23 = types.InlineKeyboardButton('23:00\n', callback_data='hora_23')

#asignaciones
clock_markup.add(clock_00,clock_01,clock_02,clock_03,clock_04,clock_05)
clock_markup.add(clock_06,clock_07,clock_08,clock_09,clock_10,clock_11)
clock_markup.add(clock_12,clock_13,clock_14,clock_15,clock_16,clock_17)
clock_markup.add(clock_18,clock_19,clock_20,clock_21,clock_22,clock_23)

#Añadir aqui nuevos markup para tener mas opciones en menu principal
start_markup.add(opt1_button)
start_markup.add(opt2_button)
start_markup.add(opt3_button)

mult_markup.add(no_button)
mult_markup.add(photo_button)
mult_markup.add(video_button)
bool_markup_send.add(si_button_send)
bool_markup_send.add(no_button_send)

#Inicio server bot

print ('-Iniciando el servidor de bot...')
time.sleep(1)
print ('-Listo!')
time.sleep(1)
print ('-Corriendo...')
calendar_1 = CallbackData("calendar_1", "action", "year", "month", "day")


#####################   HANDLER   ##################################################

def listener(messages):
        for m in messages:
                try:                              
                        if m.content_type == 'photo':
                                instance = instancefromlist(m.chat.id)
                                print("id photo: "+m.photo[2].file_id)
                                instance.img = m.photo[2].file_id
                        elif m.content_type == 'location':
                                #añadir comprobacion si es replica del mensaje puntero
                                instance = instancefromlist(m.chat.id)
                                instance.latitude =  m.location.latitude
                                instance.longitude = m.location.longitude
                        elif m.content_type == 'venue':
                                instance = instancefromlist(m.chat.id)
                                instance.latitude =  m.location.latitude
                                instance.longitude = m.location.longitude
                                instance.direccion = m.venue.title+","+m.venue.address
                        elif m.content_type == 'video':
                                instance = instancefromlist(m.chat.id)
                                print(m.video.file_id)
                                instance.vid = m.video.file_id 
                except:
                        print("Error con el mensaje m")
                        
bot.set_update_listener(listener)



################# gestión de la lista de instancias ###########################
list = []

def msgequals(obj1,obj2):
    return(obj1.user_id == obj2.user_id)

def insertList(obj):
        for x in list:
                if(msgequals(x,obj)): 
                        return False
        list.append(obj)
        return True

def instancefromlist(id_user):
        pos = getIndexfromId(id_user)
        if (pos != -1):
                return list[pos]

def getIndexfromId(id_user):
        for x in list:
                if (x.user_id == id_user):
                        return list.index(x)
        return -1

def removeListEntry(id_user):
        res = getIndexfromId(id_user)
        if( res != -1):
                del list[res] 
                return True
        return False

class msgfinal:
        user_id = ""
        action = ""
        descripcion = ""
        direccion = ""
        latitude = ""
        longitude = ""
        fecha = ""
        hora = ""
        img = ""
        vid = ""
        puntero = ""

################### FUNCTIONS ##################################################        
  
def checkmsgdata(instance,m):
        value = True
        if instance == None:
                return False
        if (instance.action == "" and instance.fecha == "" and instance.hora == ""):
                value = False
        if (instance.latitude == "" and instance.longitude == ""):
                if instance.direccion == "":
                        value = False
        return value

def sendevent(id_user,instance): #modificar el mensaje final
        msg = f"⚠‼<b>Alerta "+instance.action+"</b>‼⚠\n"
        msg += instance.descripcion +"\n"
        msg += "<b>"+instance.direccion+"</b>\n"
        if (instance.latitude != "" or instance.longitude != ""):
                msg += "https://maps.google.com/?q="+str(instance.latitude)+","+str(instance.longitude)+"\n"
        msg += "🗓" 
        msg += "<b> "+instance.fecha+"</b> - <b>"
        msg += "🕒"
        msg += instance.hora+"</b>\n"
        bot.send_message(chat_id=id_user,text=msg,parse_mode=telegram.ParseMode.HTML)
        if (instance.img != ""):
                bot.send_photo(chat_id=id_user,photo=instance.img)
        if(instance.vid != ""):
                bot.send_video(id_user,instance.vid)

def textfinal(m,instance):
        cid = m.chat.id
        msg = "Finalizar y enviar alerta?"
        instance.puntero = bot.send_message(cid,msg,reply_markup=bool_markup_send)
        

@bot.message_handler(commands=['new'])
def command_new(m):
        cid = m.chat.id
        bot.send_chat_action(cid, 'typing')
        msg = "Tema:"
        #crear aqui instancia e insertar
        instancia = msgfinal()
        instancia.user_id = m.chat.id
        instancia.puntero  = bot.send_message(cid, msg, None, None, start_markup)
        res = insertList(instancia)
        if (res == False):
                removeListEntry(m.chat.id)
        insertList(instancia)


@bot.message_handler(commands=['start'])
def command_star(m):
        cid = m.chat.id
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, DESCRIPCION, None, None)
   
@bot.message_handler(commands=['address'])
def setDireccion(m):
        instance = instancefromlist(m.chat.id)
        if (instance != None):
                tam = len(m.text)
                texto = m.text[9: 9+tam] # 9 = len("/address ")
                instance.direccion = texto

def getDireccion(m,instance):
        markup = types.InlineKeyboardMarkup(row_width=2)
        location_dir = types.InlineKeyboardButton("Ya he introducido la direccion ",callback_data="set_dir")
        markup.add(location_dir)
        bot.send_message(m.chat.id,"Escribe la dirección a mostrar en la alerta,para ello utiliza el comando /address \nej: \"/address Calle de la palmera,34\"")
        time.sleep(1.5)
        instance.puntero = bot.send_message(m.chat.id,"Una vez enviado,pulsa el boton para continuar",reply_markup=markup)
        


def getLocation(m,instance):
        markup = types.InlineKeyboardMarkup(row_width=2)
        location_act = types.InlineKeyboardButton("Ya he enviado la ubicacion",callback_data="loc_request")
        location_no = types.InlineKeyboardButton("No quiero enviar la ubicacion",callback_data="no_loc")
        markup.add(location_act)
        markup.add(location_no)
        bot.send_message(m.chat.id,"Envia la ubicacion desde la app de telegram del "+instance.action)
        time.sleep(1.5)
        instance.puntero = bot.send_message(chat_id=m.chat.id,text="Una vez enviada, pulsa el boton para continuar ", reply_markup=markup)
        
def getFecha(m):
        now = datetime.datetime.now()  # Get the current date
        bot.send_message(
                m.chat.id,
                "Introduce la fecha ",
                reply_markup=telebot_calendar.create_calendar(
                        name=calendar_1.prefix,
                        year=now.year,
                        month=now.month,  # Specify the NAME of your calendar
                ),
        )


@bot.message_handler(commands=['desc'])
def setDesc(m):
        instance = instancefromlist(m.chat.id)
        if instance != None :
                tam = len(m.text)
                texto = m.text[6: 6+tam] # 6 = "/desc "
                instance.descripcion = texto


def getDesc(m,instance):
        markup = types.InlineKeyboardMarkup()
        markup_btn = types.InlineKeyboardButton("Ya he introducido la descripcion",callback_data="desc")
        markup.add(markup_btn)
        bot.send_message(m.chat.id,"Escribe una descripcion para la alerta, para ello utiliza el comando /desc \n\nEjemplo: \"/desc hay un "+instance.action+" al que es muy importante acudir\"")
        time.sleep(1.2)
        instance.puntero = bot.send_message(m.chat.id,"Una vez enviado,pulsa el boton para continuar",reply_markup=markup)

def getHora(m,instance):
        instance.puntero = bot.send_message(m.chat.id,"¿A que hora es? ",reply_markup=clock_markup)
        
def getMult(m,instance):
        msg = "Desea adjuntar una archivo multimedia?"
        instance.puntero = bot.send_message(m.chat.id, msg,reply_markup=mult_markup)
        
def selected_opt(m,instance):
        #lo que ocurre al pulsar desnonament
        cid = m.chat.id
        texto = "Tema: "+instance.action
        bot.send_message(m.chat.id,texto)
        bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
        getDesc(m,instance)
       
###################  Callback  ############################### - con esto se procesan las llamadas inline


@bot.callback_query_handler(func=lambda call: call.data.startswith(calendar_1.prefix))
def callback_inline(call: CallbackQuery):
    instance = instancefromlist(call.from_user.id)
    # At this point, we are sure that this calendar is ours. So we cut the line by the separator of our calendar
    name, action, year, month, day = call.data.split(calendar_1.sep)
    # Processing the calendar. Get either the date or None if the buttons are of a different type
    date = telebot_calendar.calendar_query_handler(
        bot=bot, call=call, name=name, action=action, year=year, month=month, day=day
    )
    # There are additional steps. Let's say if the date DAY is selected, you can execute your code. I sent a message.
    if action == "DAY":
        bot.send_message(
            chat_id=call.from_user.id,
            text=f"Fecha: {date.strftime('%d.%m.%Y')}",
            reply_markup=ReplyKeyboardRemove(),
        )
        print(f"{calendar_1}: Day: {date.strftime('%d.%m.%Y')}")
        #encontrar la puta forma de guardar la fecha y poner aqui
        instance.fecha = date.strftime('%d.%m.%Y')
        #llamada a hora
        getHora(call.message,instance)
        
    elif action == "CANCEL":
        bot.send_message(
            chat_id=call.from_user.id,
            text="Cancelado",
            reply_markup=ReplyKeyboardRemove(),
        )
        print(f"{calendar_1}: Cancellation")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery):
    if call.message:
        instance = instancefromlist(call.from_user.id)
        if call.data == "concierto": 
                instance.action = "concierto"
                selected_opt(call.message,instance)
        elif call.data == "charla":
                instance.action = "charla"
                selected_opt(call.message,instance)
        elif call.data == "espectaculo":
                instance.action = "espectaculo"
                selected_opt(call.message,instance)
        if call.data.startswith('hora'):
                instance.hora = call.data.split('_')[1]
                bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                clock_min_markup = types.InlineKeyboardMarkup()
                clock_min_00 = types.InlineKeyboardButton(instance.hora+":00\n", callback_data='min_00')
                clock_min_15 = types.InlineKeyboardButton(instance.hora+':15\n', callback_data='min_15')
                clock_min_30 = types.InlineKeyboardButton(instance.hora+':30\n', callback_data='min_30')
                clock_min_45 = types.InlineKeyboardButton(instance.hora+':45\n', callback_data='min_45')
                clock_min_markup.add(clock_min_00,clock_min_15,clock_min_30,clock_min_45)
                texto = "Hora: "+instance.hora
                instance.puntero = bot.send_message(
                    chat_id=call.from_user.id,
                    text=texto,
                    reply_markup=clock_min_markup,
                )
               
        if call.data.startswith('min'):
                instance.hora = instance.hora+":"+call.data.split('_')[1]
                texto = "Hora: "+instance.hora
                bot.send_message(
                    chat_id=call.from_user.id,
                    text=texto,
                    reply_markup=ReplyKeyboardRemove(),
                )
                bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                getLocation(call.message,instance)
        if call.data.startswith('mult'):
                response = call.data.split('_')[1]
                bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                if (response == "no"): #suponiendo que sea lo ultimo a lo que se llama
                        textfinal(call.message,instance)
                elif(response == "photo"):
                        markup = types.InlineKeyboardMarkup()
                        markup_reply = types.InlineKeyboardButton("Ya he enviado la foto!",callback_data="mult_send")
                        markup.add(markup_reply)
                        instance.puntero = bot.send_message(call.from_user.id,"!!Envia la imagen que quieres adjuntar a la alerta",reply_markup=markup)
                elif(response == "video"):
                        markup = types.InlineKeyboardMarkup()
                        markup_reply = types.InlineKeyboardButton("Ya he enviado el video",callback_data="mult_send")
                        markup.add(markup_reply)
                        instance.puntero = bot.send_message(call.from_user.id,"!!Envia el video que quieres adjuntar a la alerta",reply_markup=markup)
                elif(response == "send"):
                        textfinal(call.message,instance)
        if call.data == "loc_request":
                bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                if instance.direccion == "":
                        getDireccion(call.message,instance)
                else:
                        getMult(call.message,instance)
        if call.data == "no_loc":
                bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                getDireccion(call.message,instance)
        if call.data == "set_dir":
                 bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                 getMult(call.message,instance)
        if call.data == "desc":
                 #obtain instnace
                 instance = instancefromlist(call.from_user.id)
                 bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                 #setDescripcion
                 getFecha(call.message)
        if call.data == "send_si":
                if(checkmsgdata(instance,call.message)):
                        #sendevent(call.from_user.id,instance) #to user reply  
                        sendevent(send_to,instance) #to target
                else:
                        bot.send_message(call.from_user.id,"Error al procesar alerta,vuelve a intentarlo")
                if instance != None:
                        bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                #borrar instancia de la lista
                removeListEntry(call.from_user.id)
        if call.data == "send_no":
                if instance != None:
                        bot.delete_message(chat_id=instance.puntero.chat.id,message_id=instance.puntero.message_id)
                bot.send_message(call.from_user.id,"No se ha enviado la alerta")
                #borrar instancia de la lista
                removeListEntry(call.from_user.id)

bot.polling(none_stop=True) #Importante pa que no se cierre y se mantenga a la escucha
