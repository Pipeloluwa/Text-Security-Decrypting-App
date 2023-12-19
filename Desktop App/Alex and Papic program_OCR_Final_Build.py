import tkinter as tk
from tkinter import ttk
#import tkinter.font as font
from tkinter import font
from tkinter import *
import cv2
import pytesseract
import random
pytesseract.pytesseract.tesseract_cmd = r"c:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def application(*g):
                
                
                


                sty=ttk.Style()
                sty.configure("Danger.TFrame",borderwidth=5,relief="sunken",background="burlywood3")
                




                mmf=tk.Frame(mw,background="darkslategray")
                flb=ttk.Frame(mmf,style="Danger.TFrame",borderwidth=12,relief="solid")
                lb5=tk.Label(flb,text=" If this screen is completely Brown, it might be you have not started the Camera yet\nAND if the screen displays Orange after you have started the Camera,\ncheck if the Camera is properly connected",
                             background="burlywood3",foreground="black")
                lb=tk.Label(flb,background="burlywood3",borderwidth=4)
                lb["height"]=20
                lb["width"]=55
                fm2=tk.Frame(mmf,borderwidth=7,relief="sunken",background="burlywood4")
                
      
                
                cp=cv2.VideoCapture(0)




                lb.focus()

                
                f1=1
                textc=""
                
                
                
                numb=0
                mn=-1
                global compil
                compil=""
                global kd
                kd="aaaaa"
                




                def decrypt(message, key):
                    origi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', ';', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


                    text = list(message)
                    KEY = key[:3]
                    length = len(text)


                    B_key = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
                    C_key = ['y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
                    D_key = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
                    E_key = ['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
                    F_key = ['v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
                    G_key = ['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
                    H_key = ['t', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
                    I_key = ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
                    J_key = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
                    K_key = ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '[', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
                    L_key = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
                    M_key = ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
                    N_key = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
                    O_key = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
                    P_key = ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
                    Q_key = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                    R_key = ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', '!', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', ':', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
                    S_key = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '\'', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', '0', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                    T_key = ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', '"', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', ')', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
                    U_key = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '/', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', '}', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F']
                    V_key = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '?', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', '\\', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E']
                    W_key = ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', '.', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', ']', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D']
                    X_key = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '>', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', '|', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C']
                    Y_key = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', ',', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', '{', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B']
                    Z_key = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', ',', '>', '.', '?', '/', '"', '\'', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', '<', '{', '|', ']', '\\', '}', ')', '0', ':', ';', ' ', '~', '`', '_', '-', '+', '=', '[', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A']

                    def main():
                        nonlocal numb
                        dencAlex()
                        global dtcad
                        dtcad=""
        
                        for n in range(length):
                            dt=(text[n])
                            dtc=str(dt)
                            dtcad=dtcad+dtc
                     
                        cv2.putText(img,dtcad,(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
                        """
                        txt2["state"]="normal"
                        if numb==0:
                            txt2.insert("1.0",dtcad)
                        if numb>=1:
                            txt2.delete=("1.0",tk.END)
                            txt2.insert("1.0",dtcad)
                        """
                        numb=numb+1
                        
            


                    def dencAlex():
                        if KEY == 'u2r':
                            dencB()
                        elif KEY == 'b90':
                            encC()
                        elif KEY == 'oot':
                            encD()
                        elif KEY == 'y7n':
                            encE()
                        elif KEY == '115':
                            encF()
                        elif KEY == 'in3':
                            encG()
                        elif KEY == 'tv5':
                            encH()
                        elif KEY == 'jxs':
                            encI()
                        elif KEY == 'l85':
                            encJ()
                        elif KEY == 'nu7':
                            encK()
                        elif KEY == 'dqr':
                            encL()
                        elif KEY == 'yb0':
                            encM()
                        elif KEY == 'il7':
                            encN()
                        elif KEY == 'avv':
                            encO()
                        elif KEY == 'zm0':
                            encP()
                        elif KEY == 're5':
                            encQ()
                        elif KEY == 'uno':
                            encR()
                        elif KEY == 'qw3':
                            encS()
                        elif KEY == 'oli':
                            encT()
                        elif KEY == '37v':
                            encU()
                        elif KEY == '5m6':
                            encV()
                        elif KEY == '08n':
                            encW()
                        elif KEY == 'ly4':
                            encX()
                        elif KEY == 'gfu':
                            encY()
                        elif KEY == 'cfg':
                            encZ()


                    def dencB():
                        for x in range(length):
                            total = 0
                            while text[x] != B_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encC():
                        for x in range(length):
                            total = 0
                            while text[x] != C_key[total]:
                                total += 1
                            text[x] = origi[total]


                    def encD():
                        for x in range(length):
                            total = 0
                            while text[x] != D_key[total]:
                                total += 1
                            text[x] = origi[total]


                    def encE():
                        for x in range(length):
                            total = 0
                            while text[x] != E_key[total]:
                                total += 1
                            text[x] = origi[total]


                    def encF():
                        for x in range(length):
                            total = 0
                            while text[x] != F_key[total]:
                                total += 1
                            text[x] = origi[total]


                    def encG():
                        for x in range(length):
                            total = 0
                            while text[x] != G_key[total]:
                                total += 1
                            text[x] = origi[total]


                    def encH():
                        for x in range(length):
                            total = 0
                            while text[x] != H_key[total]:
                                total += 1
                            text[x] = origi[total]


                    def encI():
                        for x in range(length):
                            total = 0
                            while text[x] != I_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encJ():
                        for x in range(length):
                            total = 0
                            while text[x] != J_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encK():
                        for x in range(length):
                            total = 0
                            while text[x] != K_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encL():
                        for x in range(length):
                            total = 0
                            while text[x] != L_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encM():
                        for x in range(length):
                            total = 0
                            while text[x] != M_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encN():
                        for x in range(length):
                            total = 0
                            while text[x] != N_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encO():
                        for x in range(length):
                            total = 0
                            while text[x] != O_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encP():
                        for x in range(length):
                            total = 0
                            while text[x] != P_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encQ():
                        for x in range(length):
                            total = 0
                            while text[x] != Q_key[total]:
                                total += 1
                            text[x] = origi[total]


                    def encR():
                        for x in range(length):
                            total = 0
                            while text[x] != R_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encS():
                        for x in range(length):
                            total = 0
                            while text[x] != S_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encT():
                        for x in range(length):
                            total = 0
                            while text[x] != T_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encU():
                        for x in range(length):
                            total = 0
                            while text[x] != U_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encV():
                        for x in range(length):
                            total = 0
                            while text[x] != V_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encW():
                        for x in range(length):
                            total = 0
                            while text[x] != W_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encX():
                        for x in range(length):
                            total = 0
                            while text[x] != X_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encY():
                        for x in range(length):
                            total = 0
                            while text[x] != Y_key[total]:
                                total += 1
                            text[x] = origi[total]



                    def encZ():
                        for x in range(length):
                            total = 0
                            while text[x] != Z_key[total]:
                                total += 1
                            text[x] = origi[total]



                    main()


                global cm
                def img2(*g):
                    global cm
                    global img
                    global x
                    global y
                    img=cv2.cvtColor(cp.read()[1],cv2.COLOR_BGR2RGB)
                    hImg,wImg, =img.shape[0],img.shape[1]
                    boxes=(pytesseract.image_to_data(img))

                
                    for x,b in enumerate(boxes.splitlines()):
                                if x != 0:
                                    b=b.split()
                                    if len(b)==12:
                                        x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                                        cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)

                                        getTxt=str(b[11])
                                        for i in getTxt:
                                            if i=="_" or i=='a' or i=='b' or i=='c' or i=='d' or i=='e' or i=='f' or i=='g' or i=='h' or i=='i' or i=='j' or i=='k' or i=='l' or i=='m' or i=='n' or i=='o' or i=='p' or i=='q' or i=='r' or i=='s' or i=='t' or i=='u' or i=='v' or i=='w' or i=='x' or i=='y' or i=='z' or i=='A' or i=='B' or i=='C' or i=='D' or i=='E' or i=='F' or i=='G' or i=='H' or i=='I' or i=='J' or i=='K' or i=='L' or i=='M' or i=='N' or i=='O' or i=='P' or i=='Q' or i=='R' or i=='S' or i=='T' or i=='U' or i=='V' or i=='W' or i=='X' or i=='Y' or i=='Z' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=="0":
                                                global compil
                                                compil=compil+i
                                        global dcp
                                        dcp()
                                        global kd
                                        kd=kd
                                        if len(kd) >=3:
                                            if kd[0] =="a" and kd[1] == "v" and kd[2] == "v":
                                                decrypt(compil,kd)
                                            else:
                                                cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
                                        else:
                                            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
                                        compil=""
                
                                




                    imga=Image.fromarray(img)
                    imgtk= ImageTk.PhotoImage(image = imga)
                    lb.imgtk= imgtk
                    lb.configure(image=imgtk)
                    lb.after(1,img2)
                    
    
                    
                    








                
                global ic
                ic=0
                chk=0
                chk2=0

                
                global dcp
                def dcp():
                    etg=ent.get()
                    global kd
                    kd=str(etg)
                    
                    
                    
                    
                def qt(*g):
                    mw.destroy()

                """
                def ps(*g):
                        txt["state"]="disabled"
                """        

                        

                        



                st=ttk.Style()
                st.configure("my.TButton",font=("Helvetica",10))


                
                ent=tk.Entry(fm2,relief="sunken",borderwidth=3)
            
                qtb=tk.Button(fm2,text="Quit",command=qt,borderwidth=3,font=(10),background="gray10",foreground="red")

                



                lb4=tk.Label(fm2,text="Provide key:",relief="sunken",background="burlywood3",foreground="black")


                def sc():
                    lb["height"]=0
                    lb["width"]=0
                    lb["relief"]="sunken"
                    lb5["text"]= " CAMERA  (Make Sure the text is sharp and within the camera boundary)"
                    img2()
                    btn["state"]= "disabled"

                def cbc():
                    global ic
                    ic=ic+1
                    nonlocal ent
                    entg2=ent.get()
                    gcb=cbv.get()
                    global sg
                    sg=str(gcb)
                    if sg=="on":
                        ent.destroy()
                        ent=tk.Entry(fm2,relief="sunken",borderwidth=3)
                        ent.insert("0",entg2)
                        ent.grid(row=0,column=1)
                    if sg=="off":
                        ent["show"]="*"
                cbv=StringVar()
                cbv.set("off")
                cb=tk.Checkbutton(fm2,text="Show Key",variable=cbv,command=cbc,onvalue="on",offvalue="off",
                                  relief="ridge",borderwidth=2,background="burlywood4")
                btn=tk.Button(mmf,text="Start Camera",command=sc,relief="ridge",borderwidth=5,
                              background="gray10",foreground="greenyellow")
                

                

        
                
                ent["show"]="*"

                #img2()
                flb.grid(row=0,column=0,sticky="s")
                lb5.grid(row=0,column=0)
                lb.grid(row=1,column=0)


                
                fm2.grid(row=2,column=0,sticky="n",pady=25)
                lb4.grid(row=0,column=0)
                ent.grid(row=0,column=1)
                cb.grid(row=0,column=2,padx=5)
                qtb.grid(row=0,column=3)
                btn.grid(row=1,column=0,sticky="n",pady=5)


    

                mmf.grid(row=0,column=0,sticky="nsew")
                


                mw.rowconfigure(0,minsize=100,weight=1)
                mw.columnconfigure(0,minsize=100,weight=1)

                mmf.rowconfigure([0,2],minsize=100,weight=1)
                mmf.columnconfigure(0,minsize=100,weight=1)


                
                


mw=Tk()
mw.geometry("700x500")

mw.rowconfigure(0,minsize=100,weight=1)
mw.columnconfigure(0,minsize=100,weight=1)


def dst(*g):
                canvas.destroy()
                lb.destroy()
                lb2.destroy()
                lb3.destroy()
                lb4.destroy()
                lb5.destroy()
                lb6.destroy()
                lb7.destroy()
                btn.destroy()
                application()


from PIL import Image,ImageTk
pic=Image.open("bg.png").resize((2000,1200))
bg=ImageTk.PhotoImage(pic)
canvas= tk.Canvas(mw,width=10000, height=10000)
canvas.grid(row=0,column=0)
Canvas_Image=canvas.create_image(0,0, image=bg, anchor="nw")
lb=ttk.Label(mw,text="DECRYPTING APPLICATION",background="black",foreground="NavajoWhite",font=("TkHeadingFont",25),relief="solid",borderwidth=10)
lb.grid(row=0,column=0,sticky="n",pady=40)
lb2=tk.Label(mw,text="INSTRUCTIONS AND NOTICES FOR APP USAGE (MUST READ):",relief="ridge",font=("TkCaptionFont",15),background="black",foreground="OrangeRed3")
lb2.grid(row=0,column=0,sticky="n",pady=150)
lb3=tk.Label(mw,font=("Arial"),background="black",foreground="white",text="The tendency of a correct extraction of the text depends on the quality of the camera, the angle you hold the camera,the quality of the image and absence \n of non-uniform shadow. However, capturing text on a printed paper with a plain background distinct from the text color will produce the best result.\nDO NOT CAPTURE BEYOND THE TEXT AREA,FOR EXAMPLE,DO NOT CAPTURE BEYOND THE PAPER BACKGROUND.")
lb3.grid(row=0,column=0,sticky="n",pady=200)
lb4=tk.Label(mw,font=("Arial"),background="black",foreground="white",text="HOW TO USE: Hold the Camera tightly and click just once on the picture in the camera to capture,after capturing wait for few seconds for the text extraction.\n It is better that the picture is not taken at once but in a group of few lines of text because the closer the picture to the Camera the better the result")
lb4.grid(row=0,column=0,sticky="n",pady=300)
btn=tk.Button(mw,text="CLICK HERE TO RUN THE APP",background="black",command=dst,foreground="PaleGreen",font=("TkDefaultFont",15),borderwidth=5)
btn.grid(row=0,column=0,sticky="s",pady=300)
lb5=tk.Label(mw,text="CREATED BY: \nAlex and Papic",background="black",foreground="NavajoWhite",relief="raised")
lb5.grid(row=0,column=0,sticky="s",pady=100)
lb6=tk.Label(mw,text="POWERED BY: ROBOTICS AND ARTIFICIAL INTELLIGENCE (RAIN)",background="black",foreground="NavajoWhite")
lb6.grid(row=0,column=0,sticky="s",pady=60)
lb7=tk.Label(mw,text="Alpha Version",background="black",foreground="OrangeRed3")
lb7.grid(row=0,column=0,sticky="s",pady=15)
mw.title("Decrypting Application")
mw.mainloop()


