{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "27ea7834",
   "metadata": {},
   "source": [
    "### 1. Write a Python program to check the validity of password input by users.\n",
    "Validation :\n",
    "• At least 1 letter between [a-z] and 1 letter between [A-Z].\n",
    "• At least 1 number between [0-9].\n",
    "• At least 1 character from [$#@].\n",
    "• Minimum length 6 characters\n",
    "• Maximum length 16 characters.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "49854d68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dws24$f\n",
      "7\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Length of password should be in the range 6-16 characters!'"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def password(password):\n",
    "    print(len(password))\n",
    "    if len(password) >= 6 and len(password)< 16:\n",
    "        if '#' or '@' or '$' in password:# and password.isalnum():\n",
    "            if password.isalnum():\n",
    "                return 'Valid Password'\n",
    "            else:\n",
    "                return 'Length of password should be in the range 6-16 characters!'\n",
    "        else:\n",
    "            return 'Invalid Password: Password must contain atleast one of  [$#@] characters'\n",
    "    else:\n",
    "        return 'Invalid Password() '\n",
    "        \n",
    "\n",
    "n = input()\n",
    "password(n)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f6e3d411",
   "metadata": {},
   "source": [
    "### 3. Write a Python program to check a triangle is equilateral, isosceles or scalene. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "45527916",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the length of 1st side: 54.3\n",
      "Enter the length of 2nd side: 34.5\n",
      "Enter the length of 3rd side: 75.4\n",
      "scalene Triangle\n"
     ]
    }
   ],
   "source": [
    "def triangleChecks(x,y,z):\n",
    "    if x+y>z and x+z>y and y+z>x:\n",
    "        if x==y==z:\n",
    "            print('An equilateral triangle')\n",
    "        elif x==y!=z or x!=y==z or x==z!=y:\n",
    "            print('An isosceles triangle')\n",
    "        else: \n",
    "            print('scalene Triangle')\n",
    "    else:\n",
    "        print('Triangle cannot be formed with these measures')\n",
    "\n",
    "x = float(input('Enter the length of 1st side: '))\n",
    "y = float(input('Enter the length of 2nd side: '))\n",
    "z = float(input('Enter the length of 3rd side: '))\n",
    "\n",
    "triangleChecks(x,y,z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "08fd5943",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(False, True, True)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = True,True,True\n",
    "x == True, True, True\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f487585",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ce329f3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
