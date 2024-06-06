print('\nWelcome to Babalu-Aye Consult Medical')
assistantName='Babalu'
print(f"I'm {assistantName} and I am going to help you through this process. Let start\n")
print(f"{assistantName}: Please!, Show me how I can help you,\n 1.Emergency \n 2.Consult")
informationUserEmergency=[]
nameUser=''
phoneUser=''
emergencyKindUser=''
savedInfoUser=''


try:
  answerUser=int(input('Please!,write 1 for emergency or 2 for Consulting, your answer here....'))
  if answerUser==1:
     print(f"\n{assistantName}:contact this number +254111558396 is Ambulance Number for Bababu Center, it will arrive in less than an hour.\n\nPlease!, indicate your personal information \n1.Write your Name\n2.Your phone Number\n3.Your address\n4.Kind of Emergency('accident,serious sick')")
     try:
        nameUser=str(input('Your answer(your name):....'))
        phoneUser=str(input('Your phone Number(Include, Country code):.....'))
        addressUser=str(input('Your address(Country,County,Town,Community):...'))
        emergencyKindUser=str(input('The Kind of emergency("accident,serious sick..."):....'))
       
        informationUserEmergency.append(nameUser)
        informationUserEmergency.append(phoneUser)
        informationUserEmergency.append(addressUser)
        informationUserEmergency.append(emergencyKindUser)
        print(f"\n{assistantName}: Don't worry {informationUserEmergency[0]}, our Ambulance car will find you at this address {informationUserEmergency[2]}. When reaching at that place, we will contact you on {informationUserEmergency[1]}. Your emergercy case is '{informationUserEmergency[3]}'.\n'Please try to help your self or the sick person when we're coming!!!!!'\n")
      
        
     except:
        
        print('Please!, You should write words only')
  elif answerUser==2:
     print(f"\n{assistantName}: To ensure we provide you with the best assistance possible, could you kindly share some personal information with us and accept terms and conditions\n\n       tap:yes('for accepting')\n           no(for refusing)")
     
     userAccept=input('Your answer:....')
     if userAccept=='yes' or userAccept=='Yes' or userAccept=='YES':
        nameUser=str(input('Your answer(your name):....'))
        phoneUser=str(input('Your phone Number(Include, code for your contry(like: +254..)):.....'))
        SocialSecurityNumberUser=str(input('Provide your social Number(tap enter for skipping )....'))
        
        informationUserEmergency.append(nameUser)
        informationUserEmergency.append(phoneUser)
        informationUserEmergency.append(SocialSecurityNumberUser)
        print(f"\n\n {assistantName}: Thank you for providing these information, {informationUserEmergency[0]}.\n {assistantName}:If you don't mind, could you please indicate whether you're familiar with the sickness, you have.By typing '1' if you're aware of it or '2' if you're not?")
        try:
            knowDiseaseUser=int(input('your answer (either 1 or 2)....'))
            if knowDiseaseUser==1:
               print(f"\n\n{assistantName}:Thank you for your response.In africa, these are usual sickness. Could you choose one of them to share with us details about your illness?  write the number, respectivly to your sickness:\n\n 1.Maleria('Malaria is a common disease in Africa, spread by mosquitoes. It causes symptoms like fever and fatigue. Prevention methods include using mosquito nets and taking medication. Despite efforts to control it, malaria remains a big health problem in Africa.')\n\n 2.Tuberculosis'TB'('TB remains a major health issue in Africa, particularly in areas with high population density and limited access to healthcare.')\n\n 3.Diarrheal Diseases('These are often caused by poor sanitation and contaminated water sources, leading to conditions like cholera and dysentery')\n\n 4.Respiratory Infections('Pneumonia and other respiratory infections are prevalent, especially among children and those living in overcrowded or poorly ventilated environments.')\n\n 5.Neglected Tropical Diseases 'NTDs'('These include diseases like schistosomiasis, lymphatic filariasis, and onchocerciasis, which primarily affect impoverished communities in tropical regions.') ")
               try:
                  illness1=int(input('\n  Your answer...'))
                  if illness1==1:
                     print(f"\n{assistantName}:Your sickness is Maleria,\n it's important for you {informationUserEmergency[0]}, to seek medical attention promptly. Treatment usually involves prescribed medications. Rest, staying hydrated, managing symptoms, preventing transmission, and following up with healthcare providers are crucial steps for recovery. ")
                     print(f"\nThis is your prescribed medications:\n1.Chloroquine\n2.Quinine\n3.Mefloquine")
                  elif illness1==2:
                     print(f"\n{assistantName}:Your sickness is Tuberculosis'TB',\n It's important for individuals undergoing treatment for tuberculosis to take their medications exactly as prescribed by their healthcare provider and to complete the full course of treatment, even if symptoms improve. This helps to ensure that the infection is completely eradicated and reduces the risk of developing drug-resistant TB")
                     print(f"\nThis is your prescribed medications:\n1.Isoniazid\n2.Rifampin\n3.Fluoroquinolones\n4.Injectable Medications\n5.Ethambutol")
                  elif illness1==3:
                     print(f"\n{assistantName}:Your sickness is Diarrheal Diseases,\n It's important for individuals undergoing treatment for Diarrheal Diseases to take their medications exactly. You have to do an online meeting with our expert doctor. His information are:\n\n   1.Name of the doctor: Doctor Dessai\n\n   2.Specialition:Generalist Doctor\n\n   3.Meeting: online\n\n   4.Date:10/06/2024 at 02h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq")
                     print(f"\nThis is your prescribed medications:\nYour medication prescription must be given by the doctor")
                  elif illness1==4:
                     print(f"\n{assistantName}:Your sickness is Respiratory Infections,\n Treatment for respiratory infections varies depending on the specific cause and severity of the infection.You have to do an online meeting with our expert doctor. His information are:\n\n   1.Name of the doctor: Doctor Kasole\n\n   2.Specialition:Generalist Doctor\n\n   3.Meeting: online\n\n   4.Date:09/06/2024 at 02h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq")
                     print(f"\nThis is your prescribed medications:\nYour medication prescription must be given by the doctor")
                  elif illness1==5:
                     print(f"\n{assistantName}:Your sickness is Neglected Tropical Diseases 'NTDs'.These include diseases like schistosomiasis, lymphatic filariasis, and onchocerciasis, which primarily affect impoverished communities in tropical regions.\n You have to do an online meeting with our expert doctor. His information are:\n\n   1.Name of the doctor: Doctor Emily\n\n   2.Specialition:Generalist Doctor\n\n   3.Meeting: online\n\n   4.Date:11/06/2024 at 03h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq")
                     print(f"\nThis is your prescribed medications:\nYour medication prescription must be given by the doctor")
                  else:print('Your answer is not available, Please! start again.')
            

               except:
                  print('You must provider a number')
            
            elif knowDiseaseUser==2:
               print(f"\n{assistantName}:Which part of your body is suffering?")
               print(f"\n\n  1.Head\n\n  2.Neck\n\n  3.Chest\n\n  4.Stomach\n\n  5.legs\n\n  6.All the parts")
               try:
                  illness2=int(input('Write the number of where you feel pain, here....'))
                  if illness2==1:
                     print(f"\n{assistantName}: You have choose Head,You will have a physical appoitement with our mental health professional")
                     print(f"\n Doctor's information are:\n\n   1.Name of the doctor: Doctor Kambale\n\n   2.Specialition:Mental health professional\n\n   3.Meeting: Physical Meeting\n\n   4.Date:21/06/2024 at 03h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq")

                  elif   illness2==2:
                     print(f"\n{assistantName}: You have choose Neck,You will have a physical appoitement with our orthopedic surgeon")
                     print(f"\n Doctor's information are:\n\n   1.Name of the doctor: Doctor Vanny Kibeho\n\n   2.Specialition:Orthopedic surgeon\n\n   3.Meeting: Physical Meeting\n\n   4.Date:21/06/2024 at 03h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq")

                  elif   illness2==3:
                     print(f"\n{assistantName}: You have choose Chest,You will have a physical appoitement with our ortcardiologist")
                     print(f"\n Doctor's information are:\n\n   1.Name of the doctor: Doctor Ali Suleiman\n\n   2.Specialition:Orthopedic surgeon\n\n   3.Meeting: Physical Meeting\n\n   4.Date:21/06/2024 at 03h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq")

                  elif   illness2==4:
                     print(f"\n{assistantName}: You have choose Stomach,You will have a physical appoitement with our gastroenterologist")
                     print(f"\n Doctor's information are:\n\n   1.Name of the doctor: Doctor FIdele Wabenga\n\n   2.Specialition:gastroenterologist\n\n   3.Meeting: Physical Meeting\n\n   4.Date:21/06/2024 at 03h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq")   

                  elif   illness2==5:
                     print(f"\n{assistantName}: You have choose legs,You will have a physical appoitement with our orthopedic surgeon")
                     print(f"\n Doctor's information are:\n\n   1.Name of the doctor: Doctor Ali Wabenga\n\n   2.Specialition:Orthopedic Surgeon\n\n   3.Meeting: Physical Meeting\n\n   4.Date:21/06/2024 at 03h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq") 

                  elif   illness2==6:
                     print(f"\n{assistantName}: You have choose All the parts,You will have a physical appoitement with our General Practitioner")
                     print(f"\n Doctor's information are:\n\n   1.Name of the doctor: Doctor Alice Kibeho\n\n   2.Specialition:General Practitioner\n\n   3.Meeting: Physical Meeting\n\n   4.Date:21/06/2024 at 03h00 pm \n\n   5.Link of the meeting:https://meet.google.com/ray-sgmt-bqq")                  
               except:
                  print('Your answer is not a number, can you satrt again!!!!')


           
        except:
           print('Your answer is not a number(1 or 2)')
        
        
     else:print(f"{assistantName}: In order to use our service, you should accept our conditions. Thank You")
     
  else:
     print('Plese provider the correct number')
     
except:
    print('There is an error')
