
# PyRunplify

PyRunplify is a python module that has the main focus to save and store outputs from jupyter notebook execution, allowing the user to close tha browser tab when the code is executing.

It comes with an notification system that sends an email to the user when the code is finished and with the results attached.


## Instalação

install PyRunplify with pip

```bash
  pip install PyRunplify
```
or just download the source code.
    
## Uso/Exemplos
To use PyRunplify, create a new notebook and import the module :
```python
import PyRunplify

PyRunplify.init_worker(path='model_test.ipynb',
new_name='output_archive',
email="email_test@gmail.com",
passw="email_passw",
flag="gmail",
attach_handler=True)
```
init_worker is the core function, and can receive a plethora of arguments to configure your experience:

- Path* : the path to the notebook you wish to execute
- new_name : the name for the output archive
- email¹ : the email that will send the natification
- passw¹ : the password for the email
- flag : the email host ("outlook", "gmail")
- attach_handler : if you wish the results to be sent with the notification email (true of false)

*mandatory

¹PyRunplify uses the user email to send the notifications. It does note save the email and password, its just for that execution only. You're sending yourself the notification.




## Licença

[MIT](https://choosealicense.com/licenses/mit/)

