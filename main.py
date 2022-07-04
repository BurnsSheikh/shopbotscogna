import os
import datetime
import random
import sys
import shutil
from datetime import datetime
from telethon.sync import TelegramClient
from telethon import TelegramClient,events,sync,Button
from telethon import functions,types

bot = input("Inserisci un nome da applicare al file .session, se esiste hai già un file inserisci il nome del file già esistente (ESCLUSA l'estensione finale del file): ")
api_id = 10276445
api_hash = "6c166f9a2b566fde3413cacf5a5a29ad"
client = TelegramClient(bot,api_id,api_hash)
client.start()

admin_id = int("1999796584")
nome_operatore = ("👮‍♂Admin")
obbligo_canale = ('N')
if obbligo_canale == "S" or obbligo_canale == "s":
    obbligo = True
    canale_obbligo = ("@stockdiscogna")
    
elif obbligo_canale == "N" or obbligo_canale == "n":
    obbligo = False

now = datetime.now()
dataora = now.strftime("%d/%m/%Y alle ore %H:%M:%S")

@client.on(events.NewMessage)
async def my_event_handler(e):
    
    client.parse_mode = 'html'
    sender = await e.get_sender()
    userpath = "utenti/" + str(sender.id) + "/"
    text = e.text.split(' ')
    
    file = open("admin/lista_admin", "r", encoding='utf-8')
    lista_admin = file.read()
    file.close()
    
    file = open("admin/lista_ban", "r", encoding='utf-8')
    lista_ban = file.read()
    file.close()
    
    if sender.id == admin_id or lista_admin.__contains__(str(sender.id)):
        file = open("admin/stato", "r", encoding='utf-8')
        admin_stato = file.read()
        file.close()
        
        
        if admin_stato.__contains__("nome_categoria"):
            file = open("admin/stato", "r", encoding='utf-8')
            categoria_selezionata_read = file.read().splitlines()
            file.close()
            
            categoria_selezionata = categoria_selezionata_read[0]
            
            os.rename("prodotti/" + categoria_selezionata, "prodotti/" + e.text)
            
            await e.respond("✅ Operazione completata",
                buttons=[[Button.inline("🔙 Indietro", "admin_shop")]])
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
        
        
        
        
        elif admin_stato == "aggiungi_categoria":
            os.mkdir("prodotti/" + e.text)
            
            await e.respond("✅ Operazione eseguita.",
                buttons=[[Button.inline("🔙 Indietro", "admin_shop")]])
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
        
        
        
        
        elif admin_stato == "messaggio_globale":
            all_user = os.listdir("utenti/")
            all_user_count = len(all_user)
            i = -1
            
            await e.respond("✈️ Annuncio globale partito!")
            
            while i < all_user_count - 1:
                i = i + 1
                
                try:
                    await client.send_message(int(all_user[i]), e.text)
                
                except:
                    pass
                
            await e.respond("<b>✅ Post inviato</b> a tutti gli utenti.",
                buttons=[[Button.inline("🔙 Indietro", "Home_admin")]])
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
        
        
        
        
        elif admin_stato.__contains__("aggiungi_prodotto"):
            file = open("admin/stato", "r", encoding='utf-8')
            categoria_selezionata_read = file.read().splitlines()
            file.close()
            
            categoria_selezionata = categoria_selezionata_read[0]
            
            os.mkdir("prodotti/" + categoria_selezionata + "/" + e.text)
            path = "prodotti/" + categoria_selezionata + "/" + e.text + "/"
            
            file = open(path + "nome", "w", encoding='utf-8')
            file.write(e.text)
            file.close()
            
            file = open(path + "accounts", "w", encoding='utf-8')
            file.write("")
            file.close()
            
            file = open(path + "descrizione", "w", encoding='utf-8')
            file.write("✖️")
            file.close()
            
            file = open(path + "prezzo", "w", encoding='utf-8')
            file.write("0.00")
            file.close()
            
            file = open(path + "tipologia", "w", encoding='utf-8')
            file.write("account")
            file.close()
            
            await e.respond("✅ Operazione eseguita.",
                buttons=[[Button.inline("🔙 Indietro", "admin_shop")]])
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
        
        
        
        
        elif admin_stato == "aggiungi_file":
            nome_file = e.text
            await e.respond("✅ Ok il tuo file si chiamerà <b>" + nome_file + "</b>. Ora invia il file da uplodare nel database.",
                buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write(nome_file + "\naggiungi_file_upload")
            file.close()
        
        
        
        
        elif admin_stato.__contains__("aggiungi_file_upload"):
            file = open("admin/stato", "r")
            nome_file = file.read().splitlines()
            file.close()
            
            try:
                nome1 = nome_file[0].split('>')[1]
                nome2 = nome1.split('<')[0]
            except:
                nome2 = nome_file[0]
        
            if e.media:
                await e.download_media("files/" + nome2)
                
                await e.respond("✅ File caricato con successo",
                    buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            else:
                await e.respond("❌ File non valido",
                    buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
        
        
        
        
        elif admin_stato == "rimuovi_file":
            nome_file = e.text
            
            try:
                nome1 = nome_file.split('>')[1]
                nome2 = nome1.split('<')[0]
            except:
                nome2 = nome_file
            
            try:
                os.remove("files/" + nome2)
            
                await e.respond("✅ File eliminato correttamente",
                        buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                await e.respond("❌ File specificato inesistente",
                    buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
        
        
        
        
        elif admin_stato == "scarica_file":
            nome_file = e.text
            
            try:
                nome1 = nome_file.split('>')[1]
                nome2 = nome1.split('<')[0]
            except:
                nome2 = nome_file
            
            try:
                await client.send_file(admin_id, "files/" + nome2)
            
                await e.respond("✅ File inviato",
                    buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                await e.respond("❌ Il file non è presente nel database.",
                    buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
        
        
        
        
        elif admin_stato.__contains__("nome_prodotto"):
            file = open("admin/stato", "r", encoding='utf-8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "nome", "w", encoding='utf-8')
            file.truncate(0)
            file.write(e.text)
            file.close()
            
            file = open("admin/stato", "w", encoding='utf-8')
            file.write(e.text)
            file.close()
            
            os.rename(path, "prodotti/" + categoria_selezionata + "/" + e.text)
            
            file = open("admin/stato", "r", encoding='utf-8')
            stato_read = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf-8')
            file.truncate(0)
            file.write(categoria_selezionata + "\n" + stato_read.replace(prodotto_selezionato, e.text))
            file.close()
            
            
            await e.respond("✅ Nome modificato",
                    buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
        
        
        
        
        elif admin_stato.__contains__("descrizione_prodotto"):
            file = open("admin/stato", "r", encoding='utf-8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "descrizione", "w", encoding='utf8')
            file.truncate(0)
            file.write(e.text)
            file.close()
            
            file = open("admin/stato", "r", encoding='utf-8')
            stato_read = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf-8')
            file.truncate(0)
            file.write(stato_read.replace(stato[2], "").strip('\n'))
            file.close()
            
            await e.respond("✅ Descrizione modificata",
                buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
        
        
        
        
        elif admin_stato.__contains__("imposta_file"):
            file = open("admin/stato", "r", encoding='utf-8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            testo = e.text
            
            try:
                file_selezionato_try = testo.split('>')[1]
                file_selezionato = file_selezionato_try.split('<')[0]
            except:
                file_selezionato = testo
            
            try:
                file = open("files/" + file_selezionato, "r")
                file.close()
                
                file = open(path + "tipologia", "r", encoding='utf8')
                tipologia = file.read()
                file.close()
                
                file = open(path + "tipologia", "r", encoding='utf8')
                tipologia2 = file.read().splitlines()
                file.close()
                
                try:
                    check = tipologia2[1]
                    
                    file = open(path + "tipologia", "w", encoding='utf8')
                    file.truncate(0)
                    file.write(tipologia.replace(check, file_selezionato).strip("\n"))
                    file.close()
                
                except:
                    file = open(path + "tipologia", "w", encoding='utf8')
                    file.truncate(0)
                    file.write(tipologia + "\n" + file_selezionato)
                    file.close()
                
                await e.respond("✅ File impostato",
                    buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
                
                file = open("admin/stato", "r", encoding='utf-8')
                stato_read = file.read()
                file.close()
                
                file = open("admin/stato", "w", encoding='utf-8')
                file.truncate(0)
                file.write(stato_read.replace(stato[2], "").strip('\n'))
                file.close()
            
            except:
                await e.respond("❌ File specificato non trovato",
                    buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
        
        
        
        
        elif admin_stato.__contains__("pannello_account"):
            file = open("admin/stato", "r", encoding='utf-8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "accounts", "r", encoding='utf-8')
            accounts = file.read()
            file.close()
            
            if accounts == "":
                file = open(path + "accounts", "w", encoding='utf-8')
                file.truncate(0)
                file.write(e.text)
                file.close()
            
            else:
                file = open(path + "accounts", "w", encoding='utf-8')
                file.truncate(0)
                file.write(accounts + "\n" + e.text)
                file.close()
            
            await e.respond("✅ Account/s aggiunto/i alla lista",
                buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
            
            file = open("admin/stato", "r", encoding='utf-8')
            stato_read = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf-8')
            file.truncate(0)
            file.write(stato_read.replace(stato[2], "").strip('\n'))
            file.close()
        
        
        
        
        elif admin_stato.__contains__("rimuovi_account"):
            file = open("admin/stato", "r", encoding='utf-8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "accounts", "r", encoding='utf-8')
            accounts = file.read()
            file.close()
            
            file = open(path + "accounts", "w", encoding='utf-8')
            file.truncate(0)
            file.write(accounts.replace("\n" + e.text, "").strip("\n"))
            file.close()
            
            await e.respond("✅ Account rimosso",
                buttons=[[Button.inline("🔙 Indietro", "all_account_view")]])
            
            file = open("admin/stato", "r", encoding='utf-8')
            stato_read = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf-8')
            file.truncate(0)
            file.write(stato_read.replace(stato[2], "").strip('\n'))
            file.close()
        
        
        
        
        elif admin_stato.__contains__("prezzo_prodotto"):
            file = open("admin/stato", "r", encoding='utf-8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            try:
                if e.text.__contains__(","):
                    prezzo = float(e.text.replace(",", "."))
                
                else:
                    prezzo = float(e.text)
                
                file = open(path + "prezzo", "w")
                file.truncate(0)
                file.write(str(format(prezzo, ".2f")))
                file.close()
                
                await e.respond("✅ Prezzo inserito correttamente",
                    buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
                
                file = open("admin/stato", "r", encoding='utf-8')
                stato_read = file.read()
                file.close()
                
                file = open("admin/stato", "w", encoding='utf-8')
                file.truncate(0)
                file.write(stato_read.replace(stato[2], "").strip('\n'))
                file.close()
            
            except:
                await e.respond("<b>ERRORE</b>\n\nInserisci un prezzo valido, Esempio: 1,50.",
                    buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
        
        
        
        
        elif admin_stato == "get_info_user":
            try:
                id_user = int(e.text)
                path = "utenti/" + str(id_user) + "/"
                
                file = open(path + "saldo", "r", encoding='utf-8')
                saldo = file.read()
                file.close()
                
                file = open(path + "dataavvio", "r", encoding='utf-8')
                dataavvio = file.read()
                file.close()
                
                saldo_attuale = float(saldo)
                saldo_attuale_finale = str(format(saldo_attuale,".2f"))
                
                await e.respond("👤 <b>" + str(id_user) + "</b>\n\n💰 Saldo disponibile: " + saldo_attuale_finale.replace(".", ",") + " EUR\n🕖 Primo avvio del BOT: " + dataavvio,
                    buttons=[[Button.inline("🕖 Ordini", "get_cronologia_user" + " " + str(id_user))],
                        [Button.inline("🔙 Indietro", "get_info_user")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                pass
        
        
        
        
        elif admin_stato == "add_saldo":
            try:
                id_user = int(text[0])
                
                if e.text.__contains__(","):
                    credito = float(text[1].replace(",", "."))
                
                else:
                    credito = float(text[1])
                
                path = "utenti/" + str(id_user) + "/"
                
                file = open(path + "saldo", "r", encoding='utf-8')
                saldo = file.read()
                file.close()
                
                saldo_attuale = float(saldo)
                
                calcolo = saldo_attuale + credito
                
                file = open(path + "saldo", "w", encoding='utf-8')
                file.truncate(0)
                file.write(str(format(calcolo, ".2f")))
                file.close()
                
                
                file = open(path + "cronologia", "r", encoding='utf-8')
                cronologia = file.read()
                file.close()
                
                credito_str = str(format(credito, ".2f"))
                
                file = open(path + "cronologia", "w", encoding='utf-8')
                file.truncate(0)
                file.write(cronologia + "\n\n\n• <i>Sono stati aggiunti " + credito_str.replace(".", ",") + "€ il " + dataora + "</i>")
                file.close()
                
                await e.respond("✅ Saldo aggiunto correttamente " + credito_str.replace(".", ",") + " € all'utente " + str(id_user),
                     buttons=[[Button.inline("🔙 Indietro", "admin_utenti")]])
                
                await client.send_message(int(id_user), "Il tuo credito è stato aggiornato. +" + credito_str.replace(".", ",") + " €",
                    buttons=[[Button.inline("🏠 Vai alla Home 🏠", "homeshop")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                pass
        
        
        
        
        elif admin_stato == "rimuovi_saldo":
            try:
                id_user = int(text[0])
                
                if e.text.__contains__(","):
                    credito = float(text[1].replace(",", "."))
                
                else:
                    credito = float(text[1])
                
                path = "utenti/" + str(id_user) + "/"
                
                file = open(path + "saldo", "r", encoding='utf-8')
                saldo = file.read()
                file.close()
                
                saldo_attuale = float(saldo)
                
                calcolo = saldo_attuale - credito
                
                file = open(path + "saldo", "w", encoding='utf-8')
                file.truncate(0)
                file.write(str(format(calcolo, ".2f")))
                file.close()
                
                
                file = open(path + "cronologia", "r", encoding='utf-8')
                cronologia = file.read()
                file.close()
                
                credito_str = str(format(credito, ".2f"))
                
                file = open(path + "cronologia", "w", encoding='utf-8')
                file.truncate(0)
                file.write(cronologia + "\n\n\n➖ Rimozione saldo di " + credito_str.replace(".", ",") + " € in data: " + dataora)
                file.close()
                
                await e.respond("✅ Saldo rimosso correttamente " + credito_str.replace(".", ",") + " € all'utente " + str(id_user),
                     buttons=[[Button.inline("🔙 Indietro", "admin_utenti")]])
                
                await client.send_message(int(id_user), "Il tuo credito è stato aggiornato -" + credito_str.replace(".", ",") + " €",
                    buttons=[[Button.inline("🏠 Vai alla Home 🏠", "homeshop")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                pass
        
        
        
        
        elif admin_stato == "attiva_metodo_paypal":
            file = open("admin/pagamenti/paypal", "w", encoding='utf-8')
            file.truncate(0)
            file.write(e.text)
            file.close()
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
            
            await e.respond("✅ Metodo paypal attivato correttamente.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_paypal")]])
        
        
        
        
        elif admin_stato == "attiva_metodo_bitcoin":
            file = open("admin/pagamenti/bitcoin", "w", encoding='utf-8')
            file.truncate(0)
            file.write(e.text)
            file.close()
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
            
            await e.respond("✅ Metodo bitcoin attivato correttamente.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_bitcoin")]])
        
        
        
        
        elif admin_stato == "attiva_metodo_monero":
            file = open("admin/pagamenti/monero", "w", encoding='utf-8')
            file.truncate(0)
            file.write(e.text)
            file.close()
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
            
            await e.respond("✅ Metodo attivato e impostato correttamente.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_monero")]])
        
        
        
        
        elif admin_stato == "add_admin":
            try:
                id_utente = int(e.text)
                
                file = open("admin/lista_admin", "r", encoding='utf-8')
                admins = file.read()
                file.close()
                
                
                if admins == "":
                    file = open("admin/lista_admin", "w", encoding='utf-8')
                    file.truncate(0)
                    file.write(str(id_utente))
                    file.close()
                
                else:
                    file = open("admin/lista_admin", "w", encoding='utf-8')
                    file.truncate(0)
                    file.write(admins + "\n" + str(id_utente))
                    file.close()
                
                
                await e.respond("✅ Utente aggiunto correttamente admin.",
                    buttons=[[Button.inline("🔙 Indietro", "lista_admin")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                pass
        
        
        
        
        elif admin_stato == "remove_admin":
            try:
                id_utente = int(e.text)
                utente = str(id_utente)
                
                file = open("admin/lista_admin", "r", encoding='utf-8')
                admins = file.read()
                file.close()
                
                
                file = open("admin/lista_admin", "w", encoding='utf-8')
                file.truncate(0)
                file.write(admins.replace(utente, ""))
                file.close()
                
                
                with open('admin/lista_admin') as reader, open('admin/lista_admin', 'r+', encoding='utf-8') as writer:
                  for line in reader:
                    if line.strip():
                      writer.write(line)
                  writer.truncate()
                
                
                await e.respond("✅ Utente rimosso correttamente dalla lista admin.",
                    buttons=[[Button.inline("🔙 Indietro", "lista_admin")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                pass
        
        
        
        
        elif admin_stato == "modifica_tos":
            file = open("admin/tos", "w", encoding='utf-8')
            file.truncate(0)
            file.write(str(e.text))
            file.close()
            
            await e.respond("✅ TOS impostati con successo.",
                buttons=[[Button.inline("🔙 Indietro", "admin_tos")]])
        
        
        
        
        elif admin_stato == "ban_user":
            try:
                file = open("admin/lista_ban", "r", encoding='utf-8')
                bannati = file.read()
                file.close()
                
                file = open("admin/lista_ban", "w", encoding='utf-8')
                file.truncate(0)
                file.write(bannati + "\n" + e.text)
                file.close()
                
                await e.respond("✅ Utente bannato .",
                    buttons=[[Button.inline("🔙 Indietro", "admin_ban")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                pass
        
        
        
        
        elif admin_stato == "unban_user":
            try:
                file = open("admin/lista_ban", "r", encoding='utf-8')
                bannati = file.read()
                file.close()
                
                file = open("admin/lista_ban", "w", encoding='utf-8')
                file.truncate(0)
                file.write(bannati.replace(e.text, ""))
                file.close()
                
                with open('admin/lista_ban') as reader, open('admin/lista_ban', 'r+') as writer:
                  for line in reader:
                    if line.strip():
                      writer.write(line)
                  writer.truncate()
                
                await e.respond("✅ Utente sbannato.",
                    buttons=[[Button.inline("🔙 Indietro", "admin_ban")]])
                
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
            
            except:
                pass
    
        
        
        
        elif e.text == "/start":
            await e.respond("⚙️ <b>Pannello di Configurazione\n\n</b>Ecco il <b>pannello di configurazione</b> del tuo shop.\n\n⚠️ <i>» Se non riesci ad orientarti usa apri la guida con l'apposito bottone.</i>\n\n©️Bot sviluppato da @ScognaSeLLer", 
                buttons=[[Button.inline("👤 Gestione utenti 👤", "gestione_utenti")],
                    [Button.inline("🛍 Shop", "admin_shop"), Button.inline("File 📁", "gestione_file")],
                    [Button.inline("📣 Annuncio", "messaggio_globale"), Button.inline("Pagamenti 💳", "metodi_pagamento")],
                    [Button.inline("💎 Tos 💎", "admin_tos")]])
        
        
        
        elif text[0] == "/rispondi":
            try:
                id_utente = text[1]
                
                messaggio1 = e.text.replace(text[0], "")
                messaggio2 = messaggio1.replace(text[1], "")
                
                messaggio = messaggio2.lstrip()
                
                await client.send_message(int(id_utente), nome_operatore + ": " + messaggio)
                
                await e.respond("✅ Risposta inviata")
                
                file = open("admin/lista_admin", "r", encoding='utf8')
                admins = file.read().splitlines()
                file.close()
                
                admins_num = len(admins)
                i = -1
                
                if sender.id == admin_id:
                    pass
                
                else:
                    await client.send_message(int(admin_id), "👮 L'admin " + str(sender.id) + " ha inviato un messaggio a <a href='tg://user?id= " + id_utente + "'>l'utente</a> ID " + id_utente)
                
                while i < admins_num - 1:
                    i = i + 1
                    
                    if admins[i] == str(sender.id):
                        pass
                    
                    else:
                        await client.send_message(int(admins[i]), "👮 L'admin " + str(sender.id) + " ha inviato un messaggio a l'utente ID " + id_utente)
            
            except:
                pass
    
    ###################################
    
    
    #----------------------------------------------------------------#
    
    
    ########## SEZIONE UTENTE ##########
    
    else:
        
        if lista_ban.__contains__(str(sender.id)):
            await e.respond("🔐 <b>Sei stato bannato, questa azione non ti è permessa</b>")
        
        else:
            try:
                file = open(userpath + "verifica")
                file.close()
            
            except:
                os.mkdir(userpath)
                
                file = open(userpath + "verifica", "w")
                file.write("")
                file.close()
                
                file = open(userpath + "saldo", "w")
                file.write("0.00")
                file.close()
                
                file = open(userpath + "dataavvio", "w")
                file.write(dataora)
                file.close()
                
                file = open(userpath + "cronologia", "w")
                file.write("")
                file.close()
                
                file = open(userpath + "stato", "w")
                file.write("")
                file.close()
            
            
            
            
            ###############
            if obbligo == True:
                try:
                    result = await client(functions.channels.GetParticipantRequest(
                    channel=canale_obbligo,
                    participant=int(sender.id)
                    ))
                
                except:
                    try:
                        canale_replace = canale_obbligo.replace("@stockdiscogna", "stockdiscogna")
                    except:
                        canale_replace = canale_obbligo
                    
                    await e.respond("<b>👋🏻 Ciao per utilizzare il bot devi unirti al canale sottostante!</b>",
                        buttons=[[Button.url("📣 Canale", f"https://t.me/" + canale_replace.lstrip())],
                            [Button.inline("🔄 Aggiorna", "check_canale")]])
                    return
            
            
            file = open(userpath + "stato", "r", encoding='utf8')
            utente_stato = file.read()
            file.close()
            
            
            
            if utente_stato == "chatlive":
                if e.text == "/fgdafasfsafsaf":
                    file = open(userpath + "stato", "w")
                    file.truncate(0)
                    file.close()
                    
                    await e.respond("❌ Chat terminata",
                        buttons=[[Button.inline("🔙 Indietro", "Home")]])
                
                else:
                    await client.send_message(int(admin_id), "👤 <a href='tg://user?id=" + str(sender.id) + "'>" + sender.first_name + "</a> <pre>" + str(sender.id) + "</pre> Ha inviato il seguente messaggio\n\n<i>Per rispondere utilizza </i><code>/rispondi " + str(sender.id) + " la tua risposta </code>")
                    
                    result = await client(functions.messages.ForwardMessagesRequest(
                    from_peer='me',
                    id=[e.id],
                    to_peer=int(admin_id),
                    with_my_score=True ))
                    
                    file = open("admin/lista_admin", "r", encoding='utf-8')
                    lista_utenti = file.read().splitlines()
                    lista_utenti_num = len(lista_utenti)
                    file.close()
                    
                    i = -1
                    
                    while i < lista_utenti_num - 1:
                        i = i + 1
                        
                        await client.send_message(int(lista_utenti[i]), "👤 <a href='tg://user?id=" + str(sender.id) + "'>" + sender.first_name + "</a> <pre>" + str(sender.id) + "</pre> Ha inviato il seguente messaggio\n\n<i>Per rispondere utilizza </i><code>/rispondi " + str(sender.id) + " la tua risposta </code>")
                        
                        result = await client(functions.messages.ForwardMessagesRequest(
                        from_peer='me',
                        id=[e.id],
                        to_peer=int(lista_utenti[i]),
                        with_my_score=True ))
                
                
                
                
            elif e.text == "/start":
                file = open(userpath + "dataavvio", "r")
                data_ora_avvio = file.read()
                file.close()
                file = open(userpath + "saldo", "r")
                saldo_read = file.read()
                file.close()
                
                saldo = float(saldo_read)
                
                await e.respond("👋 Benvenuto Nello ShopBot di @ScognaSeLLer\n\n🛑Il tuo saldo è: " + str(format(saldo, ".2f")) + "€\n\n© Bot sviluppato da @ScognaSeLLer",
                    buttons=[[Button.inline("☎ Supporto ☎", "chatlive")],
                    [Button.url("✅ Feed", "https://t.me/scognafeed"), Button.inline("💵 Saldo 💵", "wallet"), Button.url("📣 News 📣", "https://t.me/stockdiscogna")],
                    [Button.inline("🛍 Shop 🛍", "shop"), Button.inline("⚠ ToS ⚠", "tos")]])

@client.on(events.CallbackQuery())
async def CallbackQuery(e):
    
    client.parse_mode = 'html'
    sender = await e.get_sender()
    userpath = "utenti/" + str(sender.id) + "/"
    user_callback = int(e.original_update.user_id)
    data_str = e.data.decode('utf-8')
    data = data_str.split(' ')
    
    file = open("admin/lista_admin", "r", encoding='utf-8')
    lista_admin = file.read()
    file.close()
    
    file = open("admin/lista_ban", "r", encoding='utf-8')
    lista_ban = file.read()
    file.close()
    
    if user_callback == admin_id or lista_admin.__contains__(str(user_callback)):
        if e.data == b"Home_admin":
            await e.edit("⚙️ <b>Pannello di Configurazione\n\n</b>Ecco il <b>pannello di configurazione</b> del tuo shop.\n\n⚠️ <i>» Se non riesci ad orientarti usa apri la guida con l'apposito bottone.</i>\n\n©️Bot sviluppato da @ScognaSeLLer", 
                buttons=[[Button.inline("👤 Gestione utenti 👤", "gestione_utenti")],
                    [Button.inline("🛍 Shop", "admin_shop"), Button.inline("File 📁", "gestione_file")],
                    [Button.inline("📣 Annuncio", "messaggio_globale"), Button.inline("Pagamenti 💳", "metodi_pagamento")],
                    [Button.inline("💎 Tos 💎", "admin_tos")]])
        
        
        
        
        elif e.data == b"admin_ban":
            file = open("admin/lista_ban", "r", encoding='utf-8')
            bannati = file.read()
            file.close()
            
            if bannati == "":
                mex = "✖️"
            
            else:
                mex = bannati
            
            await e.edit("🔐 <b>Pannello di gestione bans</b> \n\n📃 Lista utenti bannati:\n\n\n" + mex,
                buttons=[[Button.inline("🔐 Banna", "ban_user"), Button.inline("Sbanna 🔓", "unban_user")],
                    [Button.inline("🔙 Indietro", "gestione_utenti")]])
        
        
        
        
        elif e.data == b"ban_user":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("ban_user")
            file.close()
            
            await e.edit("🔐 <b>Banna un utente</b>\n\nInvia l'id dell'utente da bannare",
                buttons=[[Button.inline("🔙 Indietro", "admin_ban")]])
        
        
        
        
        elif e.data == b"unban_user":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("unban_user")
            file.close()
            
            await e.edit("🔐 <b>Sbanna un utente</b>\n\nInvia l'id dell'utente da sbannare",
                buttons=[[Button.inline("🔙 Indietro", "admin_ban")]])
        
        
        
        
        elif e.data == b"admin_tos":
            file = open("admin/tos", "r", encoding='utf-8')
            tos = file.read()
            file.close()
            
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
            
            if tos == "":
                await e.edit("Termini di servizio non impostati",
                    buttons=[[Button.inline("🎛 Imposta 🎛", "modifica_tos")],
                        [Button.inline("🔙 Indietro", "Home_admin")]])
            
            else:
                await e.edit(tos,
                    buttons=[[Button.inline("🎛 Modifica 🎛", "modifica_tos")],
                        [Button.inline("🔙 Indietro", "Home_admin")]])

        
        elif e.data == b"gestione_utenti":
            await e.edit("Pannello di gestione utenti",
                buttons=[[Button.inline("🚫 Ban 🚫", "admin_ban")],
                    [Button.inline("👥 Utenti 👥", "admin_utenti")],
                    [Button.inline("👮‍♀️ Admin 👮‍♀️", "lista_admin")],
                    [Button.inline("🔙 Indietro", "Home_admin")]])
        
        
        
        
        elif e.data == b"modifica_tos":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("modifica_tos")
            file.close()
            
            await e.edit("Invia il messaggio da impostare sul bottone TOS, formattazione valida: markdown",
                buttons=[[Button.inline("🔙 Indietro", "admin_tos")]])
        
        
        
        
        elif e.data == b"lista_admin":
            if user_callback == admin_id:
                file = open("admin/stato", "w")
                file.truncate(0)
                file.close()
                
                file = open("admin/lista_admin", "r", encoding='utf8')
                admins = file.read()
                file.close()
                
                file = open("admin/lista_admin", "r", encoding='utf-8')
                admins = file.read()
                file.close()
                
                if admins == "":
                    await e.edit("<b>👮‍♂️ Lista amministratori del bot</b>\n\n<i>⚙️ I seguenti utenti hanno accesso alle opzioni di amministrazione del bot</i>\n\n\nNessun admin oltre a te",
                        buttons=[[Button.inline("➕ Aggiungi", "add_admin"), Button.inline("Rimuovi ➖", "remove_admin")],
                            [Button.inline("🔙 Indietro", "gestione_utenti")]])
                
                else:
                    await e.edit("<b>👮‍♂️ Lista amministratori del bot</b>\n\n<i>⚙️ I seguenti utenti hanno accesso alle opzioni di amministrazione del bot</i>\n\n\n" + admins,
                        buttons=[[Button.inline("➕ Aggiungi", "add_admin"), Button.inline("Rimuovi ➖", "remove_admin")],
                            [Button.inline("🔙 Indietro", "gestione_utenti")]])
            
            else:
                await e.answer("<b> Errore, non puoi accedere a questa sezione </b>.", alert=True)
        
        
        
        
        elif e.data == b"add_admin":
            if user_callback == admin_id:
                file = open("admin/stato", "w")
                file.truncate(0)
                file.write("add_admin")
                file.close()
                
                await e.edit("</b>👮‍♂️ Aggiungi amministratore</b>\n\n<i>🛂 Invia l'id dell'utente che vuoi rendere amministratore</i>",
                    buttons=[[Button.inline("🔙 Indietro", "lista_admin")]])
            
            else:
                await e.answer("<b> Errore, non puoi accedere a questa sezione </b>.", alert=True)
        
        
        
        
        elif e.data == b"remove_admin":
            if user_callback == admin_id:
                file = open("admin/stato", "w")
                file.truncate(0)
                file.write("remove_admin")
                file.close()
                
                await e.edit("</b>👮‍♂️ Rimuovi amministratore</b>\n\n<i>🛂 Invia l'id dell'utente che vuoi rimuovere amministratore</i>",
                    buttons=[[Button.inline("🔙 Indietro", "lista_admin")]])
            
            else:
                await e.answer("<b> Errore, non puoi accedere a questa sezione </b>", alert=True)
        
        
        
        
        elif e.data == b"metodi_pagamento":
            await e.edit("<b>💳 Impostazioni metodo di pagamento </b>",
                buttons=[[Button.inline("💶 PayPal 💶", "metodo_paypal")],
                    [Button.inline("💶 BitCoin 💶", "metodo_bitcoin")],
                    [Button.inline("🔙 Indietro", "Home_admin")]])
        
        
        
        
        elif e.data == b"metodo_paypal":
            file = open("admin/pagamenti/paypal", "r", encoding='utf-8')
            paypal_status = file.read()
            file.close()
            
            pulsanti = []
            
            if paypal_status == "Disabled":
                stato = "Disabilitato"
                pulsanti.append([Button.inline("PayPal ❌", "attiva_metodo_paypal")])
            
            else:
                stato = "Abilitato"
                pulsanti.append([Button.inline("PayPal ✅", "disattiva_metodo_paypal")])
            
            
            pulsanti.append([Button.inline("🔙 Indietro", "metodi_pagamento")])
            
            await e.edit("<b>Pagamento tramite paypal</b>\n\nℹ️ Attualmente il metodo PayPal risulta <b>" + stato + "</b>",
                buttons=pulsanti)
        
        
        
        
        elif e.data == b"attiva_metodo_paypal":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("attiva_metodo_paypal")
            file.close()
            
            await e.edit("<b>💳 Impostazioni metodo di pagamento PayPal</b>\n\nInvia il testo da impostare.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_paypal")]])
        
        
        
        
        elif e.data == b"disattiva_metodo_paypal":
            file = open("admin/pagamenti/paypal", "w", encoding='utf-8')
            file.truncate(0)
            file.write("Disabled")
            file.close()
            
            await e.edit("✅ Ricarica tramite PayPal disabilitata.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_paypal")]])
        
        
        
        
        elif e.data == b"metodo_bitcoin":
            file = open("admin/pagamenti/bitcoin", "r", encoding='utf-8')
            bitcoin_status = file.read()
            file.close()
            
            pulsanti = []
            
            if bitcoin_status == "Disabled":
                stato = "Disabilitato"
                pulsanti.append([Button.inline("BitCoin ❌", "attiva_metodo_bitcoin")])
            
            else:
                stato = "Abilitato"
                pulsanti.append([Button.inline("BitCoin ✅", "disattiva_metodo_bitcoin")])
            
            
            pulsanti.append([Button.inline("🔙 Indietro", "metodi_pagamento")])
            
            await e.edit("<b>Pagamento tramite bitcoin</b>\n\nℹ️ Attualmente il metodo bitcoin risulta <b>" + stato + "</b>",
                buttons=pulsanti)

        
        
        
        
        elif e.data == b"attiva_metodo_bitcoin":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("attiva_metodo_bitcoin")
            file.close()
            
            await e.edit("<b>💳 Impostazioni metodo di pagamento BitCoin</b>\n\nInvia il testo da impostare.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_bitcoin")]])
        
        
        
        
        elif e.data == b"disattiva_metodo_bitcoin":
            file = open("admin/pagamenti/bitcoin", "w", encoding='utf-8')
            file.truncate(0)
            file.write("Disabled")
            file.close()
            
            await e.edit("✅ Ricarica tramite BitCoin disabilitata.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_bitcoin")]])
        
        
        
        
        elif e.data == b"metodo_monero":
            file = open("admin/pagamenti/monero", "r", encoding='utf-8')
            monero_status = file.read()
            file.close()
            
            pulsanti = []
            
            if monero_status == "Disabled":
                stato = "disabilitato e NON può essere utilizzato dagli utenti come metodo di ricarica del proprio saldo su " + bot_name + "."
                pulsanti.append([Button.inline("MONERO ❌", "attiva_metodo_monero")])
            
            else:
                stato = "abilitato e può essere utilizzato dagli utenti come metodo di ricarica del proprio saldo su " + bot_name + "."
                pulsanti.append([Button.inline("MONERO ✅", "disattiva_metodo_monero")])
            
            
            pulsanti.append([Button.inline("🔙 Indietro", "metodi_pagamento")])
            
            await e.edit("💳 <b>METODO MONERO (XMR)</b> 💳\n\nℹ️ Attualmente il metodo Monero risulta <b>" + stato + "</b>",
                buttons=pulsanti)
        
        
        
        
        elif e.data == b"attiva_metodo_monero":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("attiva_metodo_monero")
            file.close()
            
            await e.edit("💳 <b>METODO MONERO (XMR)</b> 💳\n\nℹ️ Invia di seguito una descrizione o un tutorial per l'utente di come effettuare il pagamento compreso il wallet o altro per farti pagare con questo metodo di pagamento.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_bitcoin")]])
        
        
        
        
        elif e.data == b"disattiva_metodo_monero":
            file = open("admin/pagamenti/monero", "w", encoding='utf-8')
            file.truncate(0)
            file.write("Disabled")
            file.close()
            
            await e.edit("✅ Metodo disabilitato correttamente.",
                buttons=[[Button.inline("🔙 Indietro", "metodo_monero")]])
        
        
        
        
        elif data[0] == "get_cronologia_user":
            id_user = data[1]
            path = "utenti/" + id_user + "/"
            
            file = open(path + "cronologia", "r", encoding='utf8')
            cronologia = file.read()
            file.close()
            
            if cronologia == "":
                await e.answer("L'utente " + id_user + " non ha effettuato nessun ordine.", alert=True)
            
            else:
                await e.respond(cronologia,
                    buttons=[[Button.inline("🗑 Chiudi pannello 🗑", "get_cronologia_user_close")]])
        
        
        
        
        elif e.data == b"get_cronologia_user_close":
            await e.delete()
        
        
        
        
        elif e.data == b"admin_utenti":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
            
            utenti = os.listdir("utenti/")
            utenti_num = len(utenti)
            i = -1
            mex = ""
            
            while i < utenti_num - 1:
                i = i + 1
                mex = mex + "\n<code>" + utenti[i] + "</code>"
                    
            await e.edit("<b>👥 Gestione utenti</b>\n\n<b>📊 Utenti totali</b> " + str(utenti_num) + "<b>\n\n<b>📃 Lista utenti:<b>\n" + mex,
                buttons=[[Button.inline("➕ Aggiungi Saldo", "add_saldo"), Button.inline("Rimuovi Saldo ➖", "rimuovi_saldo")],
                    [Button.inline("Info utente", "get_info_user")],
                    [Button.inline("🔙 Indietro", "gestione_utenti")]])
        
        
        
        
        elif e.data == b"add_saldo":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("add_saldo")
            file.close()
            
            await e.edit("➕ <b>Aggiungi saldo</b>\nInserisci l'id dell'utente e il saldo che vuoi aggiungere\n\n⌨️ <i>Esempio: 1355294968 5,50</i>",
                buttons=[[Button.inline("🔙 Indietro", "admin_utenti")]])
        
        
        
        
        elif e.data == b"rimuovi_saldo":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("rimuovi_saldo")
            file.close()
            
            await e.edit("➕ <b>Rimuovi saldo</b>\nInserisci l'id dell'utente e il saldo che vuoi rimuovere\n\n⌨️ <i>Esempio: 1355294968 5,50</i>",
                buttons=[[Button.inline("🔙 Indietro", "admin_utenti")]])
        
        
        
        
        elif e.data == b"get_info_user":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("get_info_user")
            file.close()
            
            await e.edit("👥 <b>Info Utente</b>\nInvia l'userid dell'utente che si vuole controllare.",
                buttons=[[Button.inline("🔙 Indietro", "admin_utenti")]])
        
        
        
        
        elif e.data == b"messaggio_globale":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("messaggio_globale")
            file.close()
            
            await e.edit("📣 <b>Annuncio Globale</b>\n\nInvia ora il <b>messaggio</b> che sarà inviato a <u>tutti gli utenti</u> che hanno avviato il tuo shop.\n\nℹ️ Invia il testo già <b>formattato</b>.\n\n⚠️ <i>» Questa azione è </i><i><u>irreversibile</u>, ti ricordo che puoi inviare un post </i><i><u>ogni ora</u>!</i>",
                buttons=[[Button.inline("🔙 Indietro", "Home_admin")]])
        
        
        
        
        elif e.data == b"admin_shop":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.close()
        
            categorie = os.listdir("prodotti/")
            categorie_num = len(categorie)
            i = -1
            pulsanti = [[Button.inline("➕ Crea Categoria ➕", "aggiungi_categoria")]]
            
            while i < categorie_num - 1:
                i = i + 1
                pulsanti.append([Button.inline(categorie[i], "categoria_selezionata" + categorie[i])])
            
            pulsanti.append([Button.inline("🔙 Indietro", "Home_admin")])
            
            await e.edit("<b>🛍 Acquista un prodotto\n\n</b>✅ I sottostanti bottoni indicando le categorie dei prodotti che vendo.",
                buttons=pulsanti)
        
        
        
        
        elif e.data.__contains__(b"categoria_selezionata"):
            data_callback = e.data.decode('utf-8')
            categoria_selezionata = data_callback.replace("categoria_selezionata", "")
            path = "prodotti/" + categoria_selezionata + "/"
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(categoria_selezionata)
            file.close()
            
            prodotti = os.listdir(path)
            prodotti_num = len(prodotti)
            i = -1
            pulsanti = [[Button.inline("➕ Prodotto", "aggiungi_prodotto"), Button.inline("Nome", "nome_categoria"), Button.inline("Elimina 🗑", "elimina_categoria")]]
            
            while i < prodotti_num - 1:
                i = i + 1
                pulsanti.append([Button.inline(prodotti[i], "prodotto_selezionato" + prodotti[i])])
            
            pulsanti.append([Button.inline("🔙 Indietro", "admin_shop")])
            
            await e.edit("<b>🎛 Pannello di controllo della categoria: </b><code>" + categoria_selezionata + "</code>\n\n<i>Per modificare un prodotto premi su di esso</i>",
                buttons=pulsanti)
        
        
        
        
        elif e.data == b"nome_categoria":
            file = open("admin/stato", "r", encoding='utf8')
            categoria_selezionata = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(categoria_selezionata + "\nnome_categoria")
            file.close()
            
            await e.edit("<b>✏️ Imposta il nome della categoria</b><code> " + categoria_selezionata + "</code>\n\nInvia il nuovo nome della categoria",
                buttons=[[Button.inline("🔙 Indietro", "admin_shop")]])
        
        
        
        
        elif e.data == b"elimina_categoria":
            file = open("admin/stato", "r", encoding='utf8')
            categoria_selezionata = file.read()
            file.close()
            
            await e.edit("🗑 <b>Eliminazione della categoria</b><code> " + categoria_selezionata + "</code>",
                buttons=[[Button.inline("✅ Conferma", "elimina_categoria_yes")], 
                         [Button.inline("❌ Annulla", "admin_shop")]])
        
        
        
        
        elif e.data == b"elimina_categoria_yes":
            file = open("admin/stato", "r", encoding='utf8')
            categoria_selezionata = file.read()
            file.close()
            
            shutil.rmtree("prodotti/" + categoria_selezionata + "/")
            
            await e.edit("✅ Categoria eliminata correttamente.",
                buttons=[[Button.inline("🔙 Indietro", "admin_shop")]])
        
        
        
        
        elif e.data == b"aggiungi_categoria":
            file = open("admin/stato", "w")
            file.truncate(0)
            file.write("aggiungi_categoria")
            file.close()
            
            await e.edit("✏️ Invia il nome della categoria",
                buttons=[[Button.inline("🔙 Indietro", "admin_shop")]])
        
        
        
        
        elif e.data == b"aggiungi_prodotto":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read()
            file.close()
            
            file = open("admin/stato", "r", encoding='utf8')
            categoria_selezionata = file.read().splitlines()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(stato + "\naggiungi_prodotto")
            file.close()
            
            await e.edit("<b>✏️ Invia il nome del prodotto da inserire nella categoria</b><code> " + categoria_selezionata[0] + "<code>",
                buttons=[[Button.inline("🔙 Indietro", "admin_shop")]])
        
        
        
        
        elif e.data.__contains__(b"prodotto_selezionato"):
            file = open("admin/stato", "r", encoding='utf8')
            categoria_selezionata = file.read()
            file.close()
            
            data_callback = e.data.decode('utf-8')
            prodotto_selezionato = data_callback.replace("prodotto_selezionato", "")
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(categoria_selezionata + "\n" + prodotto_selezionato)
            file.close()
            
            file = open(path + "nome", "r", encoding='utf8')
            nome = file.read()
            file.close()
            
            file = open(path + "descrizione", "r", encoding='utf8')
            descrizione = file.read()
            file.close()
            
            file = open(path + "prezzo", "r", encoding='utf8')
            prezzo = file.read()
            file.close()
            
            file = open(path + "tipologia", "r", encoding='utf8')
            tipologia = file.read().splitlines()
            file.close()
            
            if tipologia[0] == "file":
                button_type = [Button.inline("🚛 Imposta file 🚛", "imposta_file")]
            
            elif tipologia[0] == "account":
                button_type = [Button.inline("🚛 Imposta account 🚛", "pannello_account")]
            
            await e.edit("<b>ℹ️ Informazioni Prodotto:\n</b>📃Nome: " + prodotto_selezionato + "\n💲Prezzo:" + prezzo.replace(".", ",") + "€\n🎛 Tipo: " + tipologia[0] + "\n📚Descrizione: " + descrizione,
                buttons=[[Button.inline("✏️ Nome", "nome_prodotto"), Button.inline("Descrizione 📜", "descrizione_prodotto")],
                    [Button.inline("🎛 Tipo", "tipologia_prodotto"), Button.inline("Prezzo 💲", "prezzo_prodotto")],
                    button_type,
                    [Button.inline("🗑 Elimina 🗑", "elimina_prodotto")],
                    [Button.inline("🔙 Indietro", "admin_shop")]])
        
        
        
        
        elif e.data.__contains__(b"return_prodotto_scelto"):
            file = open("admin/stato", "r", encoding='utf8')
            reset = file.read()
            file.close()
            
            
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            
            try:
                check = stato[2]
                
                file = open("admin/stato", "w", encoding='utf8')
                file.truncate(0)
                file.write(reset.replace(stato[2], "").strip('\n'))
                file.close()
            
            except:
                pass
            
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "nome", "r", encoding='utf8')
            nome = file.read()
            file.close()
            
            file = open(path + "descrizione", "r", encoding='utf8')
            descrizione = file.read()
            file.close()
            
            file = open(path + "prezzo", "r", encoding='utf8')
            prezzo = file.read()
            file.close()
            
            file = open(path + "tipologia", "r", encoding='utf8')
            tipologia = file.read().splitlines()
            file.close()
            
            if tipologia[0] == "file":
                button_type = [Button.inline("🚛 Imposta file 🚛", "imposta_file")]
            
            elif tipologia[0] == "account":
                button_type = [Button.inline("🚛 Imposta account 🚛", "pannello_account")]
            
            await e.edit("<b>ℹ️ Informazioni Prodotto:\n</b>📃Nome: " + prodotto_selezionato + "\n💲Prezzo:" + prezzo.replace(".", ",") + "€\n🎛 Tipo: " + tipologia[0] + "\n📚Descrizione: " + descrizione,
                buttons=[[Button.inline("✏️ Nome", "nome_prodotto"), Button.inline("Descrizione 📜", "descrizione_prodotto")],
                    [Button.inline("🎛 Tipo", "tipologia_prodotto"), Button.inline("Prezzo 💲", "prezzo_prodotto")],
                    button_type,
                    [Button.inline("🗑 Elimina 🗑", "elimina_prodotto")],
                    [Button.inline("🔙 Indietro", "admin_shop")]])
        
        
        
        
        elif e.data == b"gestione_file":
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.close()
            
            all_file = os.listdir("files/")
            all_file_num = len(all_file)
            i = -1
            data = ""
            
            while i < all_file_num - 1:
                i = i + 1
                data = data + "\n- " + all_file[i]
            
            await e.edit("🗄</b> Gestione file</b>\n\n📃Lista file:\n\n" + data,
                buttons=[[Button.inline("⬆️ Carica", "aggiungi_file"), Button.inline("Scarica ⬇️", "scarica_file")],
                    [Button.inline("🗑 Elimina", "rimuovi_file")],
                    [Button.inline("🔙 Indietro", "Home_admin")]])
        
        
        
        
        elif e.data == b"scarica_file":
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write("scarica_file")
            file.close()
            
            await e.edit("Inserisci il file che vuoi scaricare inclusa l'estenzione.",
                buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
        
        
        
        
        elif e.data == b"aggiungi_file":
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write("aggiungi_file")
            file.close()
            
            await e.edit("Inserisci il nome che vorrai inserire al file, nel caso il nome è già utilizzato il file verrà sostituito",
                buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
        
        
        
        
        elif e.data == b"rimuovi_file":
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write("rimuovi_file")
            file.close()
            
            await e.edit("Inserisci il nome del file da rimuovere inclusa l'estenzione",
                buttons=[[Button.inline("🔙 Indietro", "gestione_file")]])
        
        
        
        
        elif e.data == b"nome_prodotto":
            file = open("admin/stato", "r", encoding='utf-8')
            stato = file.read().splitlines()
            file.close()
            
            file = open("admin/stato", "r", encoding='utf-8')
            stato2 = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(stato2 + "\nnome_prodotto")
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            await e.edit("<b>✏️ Imposta il nome dell prodotto</b><code> " + prodotto_selezionato + "</code>\n\nInvia il nuovo nome del prodotto",
                buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
        
        
        
        
        elif e.data == b"descrizione_prodotto":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            file = open("admin/stato", "r", encoding='utf8')
            stato2 = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(stato2 + "\ndescrizione_prodotto")
            file.close()
            
            await e.edit("<b>✏️ Imposta la descrizione dell prodotto</b><code> " + prodotto_selezionato + "</code>\n\nInvia la nuova descrizione del prodotto",
                buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
        
        
        
        
        elif e.data == b"elimina_prodotto":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            await e.edit("<b>🗑 Eliminazione del prodotto</b><code> " + prodotto_selezionato + "</code>",
                buttons=[[Button.inline("✅ Conferma", "elimina_prodotto_yes")], 
                         [Button.inline("❌ Annulla", "return_prodotto_scelto")]])        
        
        
        
        elif e.data == b"elimina_prodotto_yes":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            shutil.rmtree(path)
            
            await e.edit("✅ Prodotto eliminato correttamente",
                buttons=[[Button.inline("🔙 Indietro", "admin_shop")]])
        
        
        
        
        elif e.data == b"tipologia_prodotto":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "tipologia", "r", encoding='utf8')
            tipologia = file.read().splitlines()
            file.close()
            
            if tipologia[0] == "account":
                pulsanti = [[Button.inline("File ❌", "change_file"), Button.inline("Account ✅", "change_account")]]
            
            elif tipologia[0] == "file":
                pulsanti = [[Button.inline("File ✅", "change_file"), Button.inline("Account ❌", "change_account")]]
            
            pulsanti.append([Button.inline("🔙 Indietro ", "return_prodotto_scelto")])
            
            await e.edit("<b>✏️ Imposta il tipo di prodotto per </b><code>" + prodotto_selezionato + "</code>\n\n<i>Il bottone che presenta la spunta ✅ è quello attualmente impostato</i>",
                buttons=pulsanti)
        
        
        
        
        elif e.data == b"change_account":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "tipologia", "w", encoding='utf8')
            file.truncate(0)
            file.write("account")
            file.close()
            
            await e.edit("✅ Tipologia di consegna impostata su: <b>Account</b>",
                buttons=[[Button.inline("🔙 Indietro ", "tipologia_prodotto")]])
        
        
        
        
        elif e.data == b"change_file":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "tipologia", "w", encoding='utf8')
            file.truncate(0)
            file.write("file")
            file.close()
            
            await e.edit("✅ Tipologia di consegna impostata su: <b>File</b>",
                buttons=[[Button.inline("🔙 Indietro", "tipologia_prodotto")]])
        
        
        
        
        elif e.data == b"imposta_file":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            
            file = open("admin/stato", "r", encoding='utf8')
            stato_read = file.read()
            file.close()
            
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(stato_read + "\nimposta_file")
            file.close()
            
            file = open(path + "tipologia", encoding='utf8')
            file_impostato = file.read().splitlines()
            file.close()
            
            try:
                file_sel = file_impostato[1]
            
            except:
                file_sel = "Non hai impostato nessun file"
            
            await e.edit("<b>🚚 Consegna file dopo l'acquisto</b>\n📦 Prodotto: <code>" + prodotto_selezionato + "</code>\n\nAdesso invia il nome del file che vuoi impostare\n\nFile attualmente impostato: " + file_sel,
                buttons=[[Button.inline("✅ Visualizza i files ✅", "all_file_view")],
                    [Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
        
        
        
        
        elif e.data == b"all_file_view":
            files = os.listdir("files/")
            files_num = len(files)
            i = -1
            mex = ""
            
            while i < files_num - 1:
                i = i + 1
                mex = mex + "\n- " + files[i]
            
            await e.edit("📁 File presenti nel database: \n\n" + mex,
                buttons=[[Button.inline("🔙 Indietro", "imposta_file")]])
        
        
        
        
        elif e.data == b"pannello_account":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            file = open("admin/stato", "r", encoding='utf8')
            stato_read = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(stato_read + "\npannello_account")
            file.close()
            
            
            await e.edit("<b>🎛 Pannello di configurazione degli account</b>\n\nInvia gli account da impostare, un account per linea\n\nEsempio:\naccount@gmail.com:password\nsecondo@gmail.com:password ",
                buttons=[[Button.inline("Visualizza/Gestisci", "all_account_view")],
                    [Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
        
        
        
        
        
        elif e.data == b"all_account_view":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            file = open("admin/stato", "r", encoding='utf8')
            stato_read = file.read()
            file.close()
            
            try:
                check = stato[2]
                file = open("admin/stato", "w", encoding='utf8')
                file.truncate(0)
                file.write(stato_read.replace(stato[2], "").strip("\n"))
                file.close()
            
            except:
                pass
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "accounts", "r", encoding='utf-8')
            accounts = file.read()
            file.close()
            
            if accounts == "":
                await e.edit("🎛 Accounts Impostati\n\nNessun account impostato",
                    buttons=[[Button.inline("🔙 Indietro", "pannello_account")]])
            
            else:
                await e.edit("🎛 Accounts Impostati\n\n" + accounts,
                    buttons=[[Button.inline("➖ Rimuovi Account", "rimuovi_account"), Button.inline("Elimina tutti gli account 🗑", "resetta_lista")],
                        [Button.inline("🔙 Indietro", "pannello_account")]])
        
        
        
        
        elif e.data == b"resetta_lista":
            await e.edit("⚠️ <b>CONFERMA ELIMINAZIONE</b> ⚠️\n\n👀 <i>Confermi di voler resettare la lista di account presenti in questo prodotto?</i>\n\n❗️ <b>Questa azione sarà IRREVERSIBILE</b>",
                buttons=[[Button.inline("✅ Conferma", "resetta_lista_yes")], 
                         [Button.inline("❌ Annulla", "all_account_view")]])
        
        
        
        
        elif e.data == b"resetta_lista_yes":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "accounts", "w")
            file.truncate(0)
            file.close()
            
            await e.edit("✅ Eliminazione avvenuta con successo",
                buttons=[[Button.inline("🔙 Indietro", "all_account_view")]])
        
        
        
        
        elif e.data == b"rimuovi_account":
            file = open("admin/stato", "r", encoding='utf8')
            stato_read = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(stato_read + "\nrimuovi_account")
            file.close()
            
            await e.edit("Invia l'account da rimuovere.",
                buttons=[[Button.inline("🔙 Indietro", "all_account_view")]])
        
        
        
        
        elif e.data == b"prezzo_prodotto":
            file = open("admin/stato", "r", encoding='utf8')
            stato = file.read().splitlines()
            file.close()
            
            categoria_selezionata = stato[0]
            prodotto_selezionato = stato[1]
            
            path = "prodotti/" + categoria_selezionata + "/" + prodotto_selezionato + "/"
            
            file = open(path + "prezzo", "r")
            prezzo = file.read()
            file.close()
            
            file = open("admin/stato", "r", encoding='utf8')
            stato_read = file.read()
            file.close()
            
            file = open("admin/stato", "w", encoding='utf8')
            file.truncate(0)
            file.write(stato_read + "\nprezzo_prodotto")
            file.close()
            
            await e.edit("<b>💲 Invia il prezzo per il prodotto</b><code> " + prodotto_selezionato + "</code>\n\nPrezzo attuale:" + prezzo.replace(".", ",") + " €.",
                buttons=[[Button.inline("🔙 Indietro", "return_prodotto_scelto")]])
    
    ##################################
    
    
    #----------------------------------------------------------------#
    
    
    ########## SEZIONE UTENTE ##########
    
    else:
        if lista_ban.__contains__(str(user_callback)):
            await e.answer("🔐 Sei stato bannato, questa azione non ti è permessa", alert=True)
        
        else:
            if obbligo == True:
                if e.data == b"check_canale":
                    try:
                        await client(functions.channels.GetParticipantRequest(
                        channel=canale_obbligo,
                        participant=int(sender.id)))
                        await e.answer("🔓 Sbloccato")
                        await e.edit("Digita /start !")
                    
                    except:
                        await e.answer("Unisciti al canale per continuare!")
                        return
                
                try:
                    await client(functions.channels.GetParticipantRequest(
                    channel=canale_obbligo,
                    participant=int(sender.id)))
                
                except:
                    try:
                        canale_replace = canale_obbligo.replace("@stockdiscogna", "stockdiscogna")
                    except:
                        canale_replace = canale_obbligo

                    await e.edit("<b>👋🏻 Ciao per utilizzare il bot devi unirti al canale sottostante!</b>",
                        buttons=[[Button.url("📣 Canale", f"https://t.me/" + canale_replace.lstrip())],
                            [Button.inline("🔄 Aggiorna", "check_canale")]])
                    return
            
            
            
            
            if e.data == b"Home":
                file = open(userpath + "dataavvio", "r")
                data_ora_avvio = file.read()
                file.close()
                file = open(userpath + "dataavvio", "r")
                data_ora_avvio = file.read()
                file.close()
                file = open(userpath + "saldo", "r")
                saldo_read = file.read()
                file.close()
                
                saldo = float(saldo_read)
                
                await e.edit("👋 Benvenuto Nello ShopBot di @ScognaSeLLer\n\n🛑Il tuo saldo è: " + str(format(saldo, ".2f")) + "€\n\n© Bot sviluppato da @ScognaSeLLer",
                    buttons=[[Button.inline("☎ Supporto ☎", "chatlive")],
                    [Button.url("✅ Feed", "https://t.me/scognafeed"), Button.inline("💵 Saldo 💵", "wallet"), Button.url("📣 News 📣", "https://t.me/stockdiscogna")],
                    [Button.inline("🛍 Shop 🛍", "shop"), Button.inline("⚠ ToS ⚠", "tos")]])
            
            
            
            
            elif e.data == b"tos":
                file = open("admin/tos", "r", encoding='utf-8')
                tos = file.read()
                file.close()
                
                if tos == "":
                    await e.edit("❌ NESSUN TOS IMPOSTATO ❌",
                        buttons=[[Button.inline("🔙 Indietro", "Home")]])
                
                else:
                    await e.edit(tos,
                        buttons=[[Button.inline("🔙 Indietro", "Home")]])
            
            
            
            
            elif e.data == b"chatlive":
                file = open(userpath + "stato", "w")
                file.truncate(0)
                file.write("chatlive")
                file.close()
                
                await e.edit("<b> Chat di supporto avviata </b>",
                    buttons=[[Button.inline("❌ Termina", "termina-chat")]])
            
            
            
            
            elif e.data == b"termina-chat":
                file = open(userpath + "stato", "w")
                file.truncate(0)
                file.close()
                
                await e.edit("<b>Chat di supporto conclusa</b>",
                    buttons=[[Button.inline("🔙 Indietro", "Home")]])
            
            
            
            
            elif e.data == b"homeshop":
                file = open(userpath + "dataavvio", "r")
                data_ora_avvio = file.read()
                file.close()

                saldo = float(saldo_read)
                
                await e.respond("👋 Benvenuto Nello ShopBot di @ScognaSeLLer\n\n🛑Il tuo saldo è: " + str(format(saldo, ".2f")) + "€\n\n© Bot sviluppato da @ScognaSeLLer",
                    buttons=[[Button.inline("☎ Supporto ☎", "chatlive")],
                    [Button.url("✅ Feed", "https://t.me/scognafeed"), Button.inline("💵 Saldo 💵", "wallet"), Button.url("📣 News 📣", "https://t.me/stockdiscogna")],
                    [Button.inline("🛍 Shop 🛍", "shop"), Button.inline("⚠ ToS ⚠", "tos")]])
            
            
            
            
            
            elif e.data == b"wallet":
                file = open(userpath + "saldo", "r")
                saldo_read = file.read()
                file.close()
                
                saldo = float(saldo_read)
                
                await e.edit("➕ <b>Ricarica Saldo </b>\n\n<b>Ricarica il tuo saldo</b> per effettuare acquisti nel bot.\n\n🛠 <i>La </i><i><b>somma di denaro</b> in euro che invii ti sarà ricaricata al </i><b><i>saldo.</i></b>\n\n💸<b> Il tuo saldo: " + str(format(saldo, ".2f")) + "€</b>\n\n⚠️ <b>Ricorda</b> di <b>inserire il tuo ID</b> [<code>" + str(sender.id) + "</code>] nella descrizione del pagamento e di <b>eseguire uno screenshot</b> della <b>transazione</b>.",
                    buttons=[[Button.inline("➕ Ricarica ➕", "ricarica_saldo")], 
                        [Button.inline("🔖 Cronologia 🔖", "cronologia_transazioni")],
                        [Button.inline("🔙 Indietro", "Home")]])
            
            
            
            
            elif e.data == b"ricarica_saldo":
                pulsanti = []
                
                file = open("admin/pagamenti/paypal", "r", encoding='utf8')
                paypal = file.read()
                file.close()
                
                file = open("admin/pagamenti/bitcoin", "r", encoding='utf8')
                bitcoin = file.read()
                file.close()
                
                file = open("admin/pagamenti/monero", "r", encoding='utf8')
                monero = file.read()
                file.close()
                
                if paypal == "Disabled":
                    pass
                
                else:
                    pulsanti.append([Button.inline("🅿️ PAYPAL 🅿️", "ricarica_paypal")])
                
                
                if bitcoin == "Disabled":
                    pass
                
                else:
                    pulsanti.append([Button.inline("💲 BitCoin 💲", "ricarica_bitcoin")])
                
                
                if monero == "Disabled":
                    pass
                
                else:
                    pulsanti.append([Button.inline("🪙 MONERO (XMR) 🪙", "ricarica_monero")])
                
                pulsanti.append([Button.inline("🔙 Indietro", "wallet")])
                
                await e.edit("➕ <b>Ricarica Saldo </b>\n\n<b>Ricarica il tuo saldo</b> per effettuare acquisti nel bot.\n\n🛠 <i>La </i><i><b>somma di denaro</b> in euro che invii ti sarà ricaricata al </i><b><i>saldo.</i></b>\n\n⚠️ <b>Ricorda</b> di <b>inserire il tuo ID</b> [<code>" + str(sender.id) + "</code>] nella descrizione del pagamento e di <b>eseguire uno screenshot</b> della <b>transazione</b>.",
                    buttons=pulsanti)
            
            
            
            
            elif e.data == b"ricarica_paypal":
                file = open("admin/pagamenti/paypal", "r", encoding='utf-8')
                desc = file.read()
                file.close()
                
                await e.edit("💰 <b>Ricarica tramite paypal</b>\n\n" + desc,
                    buttons=[[Button.inline("🎟 Pagamento inviato 🎟", "pagamento_effettuato paypal")],
                        [Button.inline("🔙 Indietro", "ricarica_saldo")]])
            
            
            
            
            elif e.data == b"ricarica_bitcoin":
                file = open("admin/pagamenti/bitcoin", "r", encoding='utf-8')
                desc = file.read()
                file.close()
                
                await e.edit("💰 <b>Ricarica tramite bitcoin</b>\n\n" + desc,
                    buttons=[[Button.inline("🎟 Pagamento inviato 🎟", "pagamento_effettuato bitcoin")],
                        [Button.inline("🔙 Indietro", "ricarica_saldo")]])
            
            
            
            
            elif e.data == b"ricarica_monero":
                file = open("admin/pagamenti/monero", "r", encoding='utf-8')
                desc = file.read()
                file.close()
                
                await e.edit("🔄 <b>RICARICA CON MONERO (XMR)</b>🔄\n\nℹ️ " + desc,
                    buttons=[[Button.inline("✅ HO EFFETTUATO IL PAGAMENTO ✅", "pagamento_effettuato monero")],
                        [Button.inline("🔙 Indietro", "ricarica_saldo")]])
            
            
            
            
            elif data[0] == "pagamento_effettuato":
                metodo = data[1]
                
                if metodo == "paypal":
                    mex = "PayPal"
                
                elif metodo == "bitcoin":
                    mex = "BitCoin"
                
                elif metodo == "monero":
                    mex = "Monero (XMR)"
                
                await client.send_message(int(admin_id), "💰Richiesta soldi\nL'utente <a href='tg://user?id=" + str(sender.id) + "'>" + sender.first_name + "</a> [<code>" + str(sender.id) + "</code>] ha inviato una richiesta di aggiunta saldo.\n\nPagamento effettuato su: " + mex)
                
                file = open("admin/lista_admin", "r", encoding='utf8')
                admins = file.read().splitlines()
                admins_num = len(admins)
                file.close()
                i = - 1
                
                while i < admins_num - 1:
                    i = i + 1
                    await client.send_message(int(admins[i]), "💰Richiesta soldi\nL'utente <a href='tg://user?id=" + str(sender.id) + "'>" + sender.first_name + "</a> [<code>" + str(sender.id) + "</code>] ha inviato una richiesta di aggiunta saldo.\n\nPagamento effettuato su: " + mex)
                
                
                await e.edit("🧾 <b>Pagamento effettuato</b>\n\nHai <b>effettuato</b> un pagamento presso lo <b>shop</b>.\n\n📸 🕰 <i><b>Attendi</b> che un </i><i><b>amministratore</b> del bot lo visualizzi e ti </i><i><b>ricarichi il saldo</b>.</i>",
                    buttons=[[Button.inline("🏘 Home 🏘", "Home")]])
            
            
            
            
            elif e.data == b"cronologia_transazioni":
                file = open(userpath + "cronologia", "r", encoding='utf8')
                cronologia = file.read()
                file.close()
                
                if cronologia == "":
                    await e.edit("🔦 <b>Cronologia acquisti</b>\n\nLa <b>cronologia </b>degli acquisti é <b>vuota</b>!",
                        buttons=[[Button.inline("🔙 Indietro", "wallet")]])
                
                else:
                    await e.edit("<b>🔦 Cronologia acquisti<b>\n\nLa <b>cronologia</b> dei tuoi acquisti é la seguente:\n\n" + cronologia,
                        buttons=[[Button.inline("🔙 Indietro", "wallet")]])
            
            
            
            
            elif e.data == b"shop":
                categorie = os.listdir("prodotti/")
                
                if categorie == []:
                    await e.edit("❌ <b>Errore</b>\n\nNessuna categoria disponibile",
                        buttons=[[Button.inline("🔙 Indietro", "Home")]])
                
                else:
                    num_categorie = len(categorie)
                    i = -1
                    pulsanti = []
                    
                    while i < num_categorie - 1:
                        i = i + 1
                        pulsanti.append([Button.inline(categorie[i], "categoria_selezionata" + categorie[i])])
                    
                    pulsanti.append([Button.inline("🔙 Indietro", "Home")])
                    await e.edit("<b>🛍 Acquista un prodotto</b>\n\n✅ I sottostanti bottoni indicando le categorie dei prodotti che vendo.",
                        buttons=pulsanti)
            
            
            
            
            elif e.data.__contains__(b"categoria_selezionata"):
                data_callback = e.data.decode('utf-8')
                categoria_selezionata_replace = str(data_callback)
                categoria_selezionata = categoria_selezionata_replace.replace("categoria_selezionata", "")
                
                path = "prodotti/" + categoria_selezionata + "/"
                
                prodotti = os.listdir(path)
                
                if prodotti == []:
                    await e.edit("❌ <b>Errore</b>\n\nNessun prodotto disponibile nella categoria.",
                        buttons=[[Button.inline("🔙 Indietro", "Home")]])
                
                else:
                    num_prodotti = len(prodotti)
                    i = -1
                    pulsanti = []
                    
                    while i < num_prodotti - 1:
                        i = i + 1
                        try:
                            adici = os.listdir(path + prodotti[i] + "/")
                            pulsanti.append([Button.inline(prodotti[i], "prodotto_selezionato" + prodotti[i])])
                        
                        except:
                            pass
                    
                    file = open(userpath + "stato", "w", encoding='utf-8')
                    file.truncate(0)
                    file.write(categoria_selezionata)
                    file.close()
                    
                    pulsanti.append([Button.inline("🔙 Indietro", "shop")])
                    await e.edit("<b>🧮 Prodotti nella categoria " + categoria_selezionata + "</b>\n\n<i>✅ I sottostanti bottoni indicando i prodotti che vendo della categoria " + categoria_selezionata + " .<i>",
                        buttons=pulsanti)
            
            
            
            
            elif e.data.__contains__(b"prodotto_selezionato"):
                data_callback = e.data.decode('utf-8')
                prodotto_selezionato_replace = str(data_callback)
                prodotto_selezionato = prodotto_selezionato_replace.replace("prodotto_selezionato", "")
                
                file = open(userpath + "stato", "r", encoding='utf8')
                categoria = file.read()
                file.close()
                
                path = "prodotti/" + categoria + "/" + prodotto_selezionato + "/"
                
                file = open(path + "nome", "r", encoding='utf8')
                nome = file.read()
                file.close()
                
                file = open(path + "descrizione", "r", encoding='utf8')
                descrizione = file.read()
                file.close()
                
                file = open(path + "prezzo", "r", encoding='utf8')
                prezzo = file.read()
                file.close()
                
                file = open(path + "tipologia", "r", encoding='utf8')
                tipologia = file.read()
                file.close()
                
                file = open(userpath + "stato", "w", encoding='utf8')
                file.truncate(0)
                file.write(nome + "\n" + descrizione + "\n" + prezzo + "\n" + tipologia + "\n" + path)
                file.close()
                
                await e.edit("🛍 Prodotto: <b>" + nome + "</b>\n\n💲 Costo: " + prezzo.replace(".", ",") + " €\n\nℹ️ Informazioni: <b>" + descrizione + " </b>.",
                    buttons=[[Button.inline("💰 Compra", "conferma_acquisto")],
                        [Button.inline("🔎 Disponibilità", "controlla_disp")],
                        [Button.inline("🔙 Indietro", "shop")]])
            
            
            
            elif e.data == b"controlla_disp":
                file = open(userpath + "saldo", "r")
                saldo_read = file.read()
                file.close()
                
                saldo = float(saldo_read)
                
                file = open(userpath + "stato", "r", encoding='utf8')
                stato = file.read().splitlines()
                file.close()
                
                prezzo = float(stato[2])

                calcolo_finale = saldo - prezzo

                    
                try:
                    path = stato[5]
                    
                except:
                    path = stato[4]
                    
                file = open(path + "tipologia", "r", encoding='utf8')
                tipologia = file.read().splitlines()
                file.close()
                                        
                if tipologia[0] == "file":
                    await e.answer('📂 File')
                    
                elif tipologia[0] == "account":
                    file = open(path + "accounts", "r", encoding='utf8')
                    line_count = 0
                    for line in file:
                        if line != "\n":
                            line_count += 1
                    file.close()
                            
                    await e.answer(f'✅ Ci sono {line_count} account disponibili')

            
            elif e.data == b"conferma_acquisto":
                file = open(userpath + "stato", "r", encoding='utf8')
                stato = file.read().splitlines()
                file.close()
                
                await e.edit("🛒 <b>Conferma acquisto</b> ✅\n\nConfermi di voler acquistare <b>" + stato[0] + "</b> al costo di <b>" + stato[2].replace(".", ",") + " €</b>?",
                    buttons=[[Button.inline("🛒 Acquista", "acquisto_confermato")],
                             [Button.inline("🔙 Indietro", "shop")]])
            
            
            
            
            elif e.data == b"acquisto_confermato":
                file = open(userpath + "saldo", "r")
                saldo_read = file.read()
                file.close()
                
                saldo = float(saldo_read)
                
                file = open(userpath + "stato", "r", encoding='utf8')
                stato = file.read().splitlines()
                file.close()
                
                prezzo = float(stato[2])
                
                if(saldo < prezzo):
                    await e.answer("💲 Non hai il saldo sufficiente.", alert=False)
                
                elif(saldo >= prezzo):
                    calcolo_finale = saldo - prezzo
                    
                    file = open(userpath + "saldo", "w")
                    file.truncate(0)
                    file.write(str(calcolo_finale))
                    file.close()
                    
                    file = open(userpath + "cronologia", "r", encoding='utf8')
                    cronologia = file.read()
                    file.close()
                    
                    file = open(userpath + "cronologia", "w", encoding='utf8')
                    file.truncate(0)
                    file.write(cronologia + "\n\n\n• <i>Hai acquistato </i><i><u>" + stato[0] + "</u> a " + stato[2].replace(".", ",") + "€ il" + dataora + "</i>")
                    file.close()
                    
                    try:
                        path = stato[5]
                    
                    except:
                        path = stato[4]
                    
                    file = open(path + "tipologia", "r", encoding='utf8')
                    tipologia = file.read().splitlines()
                    file.close()
                    
                    await e.delete()
                    
                    if tipologia[0] == "file":
                        try:
                            file_send = "files/" + tipologia[1]
                            
                            await client.send_file(int(sender.id), file_send)
                            
                            await e.respond("✅ <b>Acquisto effettuato con successo</b>\n\nIl file lo trovi allegato al messaggio.")
                            

                        except:
                            await e.respond("✅ <b>Acquisto effettuato con successo</b>\n\nNessun prodotto è stato impostato, contatta l'assistenza per fartelo dare")
                    
                    elif tipologia[0] == "account":
                        try:
                            file = open(path + "accounts", "r", encoding='utf8')
                            line_count = -1
                            for line in file:
                                if line != "\n":
                                    line_count += 1
                            file.close()
                            
                            numero_rnd = random.randint(0,line_count)
                            
                            
                            file = open(path + "accounts", "r", encoding='utf8')
                            accounts = file.read().splitlines()
                            file.close()
                            
                            
                            file = open(path + "accounts", "r", encoding='utf8')
                            accounts_rpl = file.read()
                            file.close()
                            
                            selezionato = accounts[line_count]
                            
                            replace_acc = accounts_rpl.replace(selezionato, "").strip('\n')
                            
                            if line_count <= 0:
                                file = open(path + "accounts", "w", encoding='utf8')
                                file.truncate(0)
                                file.close()
                            
                            else:
                                file = open(path + "accounts", "w", encoding='utf8')
                                file.truncate(0)
                                file.write(replace_acc)
                                file.close()
                            
                            
                            await e.respond("✅ <b>Acquisto effettuato con successo</b>\n\nEcco il tuo account:\n\n<pre>" + accounts[line_count] + "</pre>")
                        
                        except:
                            await e.respond("✅ <b>Acquisto effettuato con successo</b>\n\nNessun prodotto è stato impostato, contatta l'assistenza per fartelo dare")
                    
                    
                    file = open("admin/lista_admin", "r", encoding='utf8')
                    admins = file.read().splitlines()
                    admins_num = len(admins)
                    file.close()
                    i = - 1
                    
                    await client.send_message(int(admin_id), "<a href='tg://user?id=" + str(sender.id) + "'>" + sender.first_name + "</a> [<code>" + str(sender.id) + "</code>] ha effettuato un acquisto.\n\n🛍 Prodotto: " + stato[0] + "\n➖ Saldo rimosso: " + stato[2].replace(".", ",") + " €")
                    
                    while i < admins_num - 1:
                        i = i + 1
                        await client.send_message(int(admin_id), "<a href='tg://user?id=" + str(sender.id) + "'>" + sender.first_name + "</a> [<code>" + str(sender.id) + "</code>] ha effettuato un acquisto.\n\n🛍 Prodotto: " + stato[0] + "\n➖ Saldo rimosso: " + stato[2].replace(".", ",") + " €")
    
    ####################################
    
    
    
    
    

client.run_until_disconnected()