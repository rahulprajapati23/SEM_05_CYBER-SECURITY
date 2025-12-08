# Cryptography Notes

> [!NOTE]
> These notes were automatically generated/extracted from the lecture PDFs.

## Lecture 10 13.8 Cryptography BMK

### Simple Notes (Key Points)
- ▪ A transposition cipher does not substitute one symbol for
- ▪ The simplest such cipher is the rail fence technique, in which the
- ▪ She then creates the ciphertext “MEMATEAKETETHPR”.
- ▪ He then creates the ciphertext “TKVMHNYUEYUHAORE”.
- ▪ The order of the columns then becomes the key to the algorithm.

### Detailed Notes
Lecture 10
Transposition Techniques

Transposition Techniques
1) Rail Fence Transposition
2) Row Column Transposition

Rail Fence Transposition
▪ A transposition cipher does not substitute one symbol for
another, instead it changes the location of the symbols.
▪ The simplest such cipher is the rail fence technique, in which the
plaintext is written down as a sequence of diagonals and then
read off as a sequence of rows.
▪ For example, to send the message “Meet me at the park” to Bob,
Alice writes
▪ She then creates the ciphertext “MEMATEAKETETHPR”.

Rail Fence Transposition
▪ For example, to send the message “Thank you very much” to
Alice, What Bob writes ? Use depth 3
▪ He then creates the ciphertext “TKVMHNYUEYUHAORE”.

Transposition Techniques
1) Rail Fence Transposition
2) Row Column Transposition

Row Column Transposition
▪ A more complex scheme is to write the message in a rectangle,
row by row, and read the message off, column by column, but
permute the order of the columns.
▪ The order of the columns then becomes the key to the algorithm.
Key:       4 3 1 2 5 6 7
Plaintext: a t t a c k p
o s t p o n e
d u n t i l t
w o a m x y z
Ciphertext: TTNAAPTMTSUOAODWCOIXKNLYPETZ

Row Column Transposition
Ciphertext: “Kill corona virus at twelve am tomorrow”
Ciphertext: “LATARLVTMOINAERKOSVOCIWTWOREOY”.


### Extracted Images
![Lecture_10_13.8_Cryptography_BMK_p3_i0.jpg](assets/Lecture_10_13.8_Cryptography_BMK_p3_i0.jpg)

---

## Lecture 11 19.8 Cryptography BMK

### Simple Notes (Key Points)
- *(No specific key points detected automatically)*

### Detailed Notes
Lecture 11
Steganography

Steganography
A plaintext message may be hidden in one of two ways.
The methods of steganography conceal the existence of the
message, whereas the methods of cryptography render the
message unintelligible to outsiders by various transformations
of the text
A simple form of steganography, but one that is time-
consuming to construct, is one in which an arrangement of
words or letters within an apparently innocuous
text spells out the real message.

Steganography
Example:
Simply encrypt correct reading exactly twice
Simply encrypt correct reading exactly twice
Secret

Steganography
1) Character marking
2) Invisible ink
3) Pin punctures
4) Typewriter correction ribbon

Character marking
Selected letters of printed or typewritten text are over
written in pencil.
The marks are ordinarily not visible unless the paper is
held at an angle to bright light.

Invisible ink
A number of substances can be used for writing but
leave no visible trace until heat or some chemical is
applied to the paper.

Pin punctures
Small pin punctures on selected letters are ordinarily
not visible unless the paper is held up in front of a light.

Typewriter correction ribbon
Used between lines typed with a black ribbon, the
results of typing with the correction tape are visible
only under a strong light.


---

## Lecture 12 20.8 Cryptography BMK

### Simple Notes (Key Points)
- *(No specific key points detected automatically)*

### Detailed Notes
Lecture 12
Modular arithmetic

Congruence

Congruence

Congruence

Congruence

Modular arithmetic

Modular arithmetic

Modular arithmetic

Modular arithmetic

Modular arithmetic


### Extracted Images
![Lecture_12_20.8_Cryptography_BMK_p2_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p2_i0.jpg)

![Lecture_12_20.8_Cryptography_BMK_p3_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p3_i0.jpg)

![Lecture_12_20.8_Cryptography_BMK_p4_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p4_i0.jpg)

![Lecture_12_20.8_Cryptography_BMK_p5_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p5_i0.jpg)

![Lecture_12_20.8_Cryptography_BMK_p6_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p6_i0.jpg)

![Lecture_12_20.8_Cryptography_BMK_p7_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p7_i0.jpg)

![Lecture_12_20.8_Cryptography_BMK_p8_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p8_i0.jpg)

![Lecture_12_20.8_Cryptography_BMK_p9_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p9_i0.jpg)

![Lecture_12_20.8_Cryptography_BMK_p10_i0.jpg](assets/Lecture_12_20.8_Cryptography_BMK_p10_i0.jpg)

---

## Lecture 14 26.8 Cryptography BMK

### Simple Notes (Key Points)
- Diffie-Hellman Key Exchange
- RSA Encryption
- we define an integral domain, which is a commutative ring that obeys the
- Homomorphic Encryption
- Finite Fields, Most cryptographic algorithms operate over finite fields

### Detailed Notes
Lecture 14
Algebric Structure

Algebraic structures
The combination of the set and the operations that are applied to the
elements of the set is called an algebraic structure
The study of three algebraic structures allows us to use sets in which
operations similar to addition/subtraction and multiplication/division can be
used with the set.
Group
Ring
Field

Group
A group is a set equipped with an operation (e.g., addition or multiplication)
that satisfies the following properties:
Closure: Performing the operation on two elements of the set results in an
element within the set.
Associativity: The operation is associative.
Identity Element: There is an element in the set such that operation with any
element leaves it unchanged.
Inverse Element: Every element has an inverse.
A1 Closure
A2 Associativity
A3 Identity
A4 Inverse Element

Group
Applications in Cryptography
Elliptic Curve Cryptography (ECC)
Diffie-Hellman Key Exchange
RSA Encryption

Finite Group &  Infinite Group
If a group has a finite number of elements, it is referred to as a finite group,
and the order of the group is equal to the number of elements in the group.
Otherwise, the group is an infinite group.
Abelian Group
A group is said to be abelian if it satisfies the following additional condition
A5 Commutative

Group

Group

Abelian Group

Notations

Group

Group

Abelian Group

Rings
A ring is an algebraic structure consisting of a set equipped with two binary
operations, typically addition and multiplication, satisfying:
Closure under multiplication
If a,b ∈ R , then ab ∈ R
Multiplication is associative.
a(bc) = (ab)c for all a , b , c in R
Multiplication distributes over addition
a(b + c) = ab + ac for all a , b , c in R .
(a + b)c = ac + bc for all a , b , c in R .
A1 - A4 Group
M1 Closure under multiplication
A5 Abelian Group
M2 Associativity of multiplication
M3 Distributive laws

Commutative Ring
A ring is said to be commutative if it satisfies the following conditions:
Commutativity of multiplication
ab = ba for all a , b in R
A1 - A4 Group
M1- M3 Ring
A5 Abelian Group
M4 Commutativity of multiplication

Integral Domain
we define an integral domain, which is a commutative ring that obeys the
following axioms
Multiplicative identity
There is an element 1 in R such that a1 = 1a = a for all a in R
A1 - A4 Group
M1- M3 Ring
A5 Abelian Group
M4 Commutativity Ring
M5 Multiplicative identity
M6 No zero divisors:
No zero divisors
If a , b in R and ab = 0 , then either a = 0 or b = 0 .

Rings
Applications in Cryptography
Lattice-based Cryptography
Homomorphic Encryption
RSA and Modular Arithmetic

Fields
A field is a ring with the additional property that every nonzero element has
a multiplicative inverse.
Multiplicative inverse
For each a in F , except 0, there is an element
a - 1 in F such that aa - 1 = (a - 1 )a = 1 .
A1 - M6 Group & Rings
M7 Multiplicative inverse

Fields
Applications in Cryptography
Finite Fields, Most cryptographic algorithms operate over finite fields
AES Encryption
Elliptic Curve Cryptography
Error-Correcting Codes
Polynomial-based Schemes


### Extracted Images
![Lecture_14_26.8_Cryptography_BMK_p6_i0.png](assets/Lecture_14_26.8_Cryptography_BMK_p6_i0.png)

![Lecture_14_26.8_Cryptography_BMK_p7_i0.jpg](assets/Lecture_14_26.8_Cryptography_BMK_p7_i0.jpg)

![Lecture_14_26.8_Cryptography_BMK_p8_i0.jpg](assets/Lecture_14_26.8_Cryptography_BMK_p8_i0.jpg)

![Lecture_14_26.8_Cryptography_BMK_p9_i0.jpg](assets/Lecture_14_26.8_Cryptography_BMK_p9_i0.jpg)

![Lecture_14_26.8_Cryptography_BMK_p10_i0.jpg](assets/Lecture_14_26.8_Cryptography_BMK_p10_i0.jpg)

![Lecture_14_26.8_Cryptography_BMK_p11_i0.jpg](assets/Lecture_14_26.8_Cryptography_BMK_p11_i0.jpg)

![Lecture_14_26.8_Cryptography_BMK_p12_i0.jpg](assets/Lecture_14_26.8_Cryptography_BMK_p12_i0.jpg)

---

## Lecture 15 29.8 Cryptography BMK

### Simple Notes (Key Points)
- Miller-Rabin Algorithm
- Miller-Rabin Algorithm
- Miller-Rabin Algorithm

### Detailed Notes
Lecture 15
Checking of primeness

Checking of Primeness
Fermat's Theorem
Miller-Rabin Algorithm

Fermat's Theorem

Fermat's Theorem

Fermat's Theorem

Miller-Rabin Algorithm

Miller-Rabin Algorithm




### Extracted Images
![Lecture_15_29.8_Cryptography_BMK_p3_i0.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p3_i0.jpg)

![Lecture_15_29.8_Cryptography_BMK_p3_i1.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p3_i1.jpg)

![Lecture_15_29.8_Cryptography_BMK_p3_i2.png](assets/Lecture_15_29.8_Cryptography_BMK_p3_i2.png)

![Lecture_15_29.8_Cryptography_BMK_p3_i3.png](assets/Lecture_15_29.8_Cryptography_BMK_p3_i3.png)

![Lecture_15_29.8_Cryptography_BMK_p3_i4.png](assets/Lecture_15_29.8_Cryptography_BMK_p3_i4.png)

![Lecture_15_29.8_Cryptography_BMK_p3_i5.png](assets/Lecture_15_29.8_Cryptography_BMK_p3_i5.png)

![Lecture_15_29.8_Cryptography_BMK_p3_i6.png](assets/Lecture_15_29.8_Cryptography_BMK_p3_i6.png)

![Lecture_15_29.8_Cryptography_BMK_p4_i0.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p4_i0.jpg)

![Lecture_15_29.8_Cryptography_BMK_p4_i1.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p4_i1.jpg)

![Lecture_15_29.8_Cryptography_BMK_p4_i2.png](assets/Lecture_15_29.8_Cryptography_BMK_p4_i2.png)

![Lecture_15_29.8_Cryptography_BMK_p4_i3.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p4_i3.jpg)

![Lecture_15_29.8_Cryptography_BMK_p5_i0.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p5_i0.jpg)

![Lecture_15_29.8_Cryptography_BMK_p5_i1.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p5_i1.jpg)

![Lecture_15_29.8_Cryptography_BMK_p5_i2.png](assets/Lecture_15_29.8_Cryptography_BMK_p5_i2.png)

![Lecture_15_29.8_Cryptography_BMK_p6_i0.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p6_i0.jpg)

![Lecture_15_29.8_Cryptography_BMK_p7_i0.png](assets/Lecture_15_29.8_Cryptography_BMK_p7_i0.png)

![Lecture_15_29.8_Cryptography_BMK_p7_i1.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p7_i1.jpg)

![Lecture_15_29.8_Cryptography_BMK_p7_i2.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p7_i2.jpg)

![Lecture_15_29.8_Cryptography_BMK_p7_i3.png](assets/Lecture_15_29.8_Cryptography_BMK_p7_i3.png)

![Lecture_15_29.8_Cryptography_BMK_p7_i4.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p7_i4.jpg)

![Lecture_15_29.8_Cryptography_BMK_p7_i5.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p7_i5.jpg)

![Lecture_15_29.8_Cryptography_BMK_p7_i6.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p7_i6.jpg)

![Lecture_15_29.8_Cryptography_BMK_p7_i7.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p7_i7.jpg)

![Lecture_15_29.8_Cryptography_BMK_p7_i8.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p7_i8.jpg)

![Lecture_15_29.8_Cryptography_BMK_p8_i0.jpg](assets/Lecture_15_29.8_Cryptography_BMK_p8_i0.jpg)

---

## Lecture 16 9.9 Cryptography BMK

### Simple Notes (Key Points)
- symmetric key ciphers
- ▪ Modern block ciphers
- ▪ Modern stream ciphers
- ▪ Data Encryption standard
- ▪ Advanced encryption standard

### Detailed Notes
UNIT- 4
Modern
symmetric key ciphers

Unit-4
▪ Modern block ciphers
▪ Modern stream ciphers
▪ Data Encryption standard
▪ Advanced encryption standard
▪ Electronic Code Book Mode
▪ Cipher Block Chaining Mode
▪ Cipher Feedback Mode
▪ Output Feedback Mode

Lecture 16
Stream Cipher

Stream Cipher
▪ A stream cipher is one that encrypts a digital data stream one bit
or one byte at a time.
▪ Examples of classical stream ciphers are Autokeyed Vigenère
cipher ,A5/1, RC4 and Vernam cipher.


### Extracted Images
![Lecture_16_9.9_Cryptography_BMK_p1_i0.png](assets/Lecture_16_9.9_Cryptography_BMK_p1_i0.png)

![Lecture_16_9.9_Cryptography_BMK_p4_i0.png](assets/Lecture_16_9.9_Cryptography_BMK_p4_i0.png)

---

## Lecture 17 10.9 Cryptography BMK

### Simple Notes (Key Points)
- Block Cipher
- Block Cipher
- ▪ A block cipher is one in which a block of plaintext is treated as a
- whole and used to produce a ciphertext block of equal length.
- ▪ Examples are Feistel Cipher, DES, Triple DES and AES

### Detailed Notes
Lecture 17
Block Cipher

Block Cipher
▪ A block cipher is one in which a block of plaintext is treated as a
whole and used to produce a ciphertext block of equal length.
▪ Typically, a block size of 64 or 128 bits is used.
▪ Examples are Feistel Cipher, DES, Triple DES and AES


### Extracted Images
![Lecture_17_10.9_Cryptography_BMK_p2_i0.png](assets/Lecture_17_10.9_Cryptography_BMK_p2_i0.png)

---

## Lecture 18 12.9 Cryptography BMK

### Simple Notes (Key Points)
- ▪ Confusion hides the relationship between the ciphertext and the
- ▪ This is achieved by the use of a complex substitution algorithm.
- ▪ Diffusion hides the relationship between the ciphertext and the
- many ciphertext digits.

### Detailed Notes
Lecture 18
Confusion and Diffusion

Confusion and Diffusion
▪ Confusion hides the relationship between the ciphertext and the
key.
▪ Making relationship between EK and CT as complex as possible.
▪ This is achieved by the use of a complex substitution algorithm.
▪ Example: Substitution
▪ Diffusion hides the relationship between the ciphertext and the
plaintext.
▪ This is achieved by having each plaintext digit affect the value of
many ciphertext digits.
▪ Examples: Transpositions or Permutation


---

## Lecture 19 16.9 Cryptography BMK

### Simple Notes (Key Points)
- symmetric key ciphers
- ▪ Modern block ciphers
- ▪ Modern stream ciphers
- ▪ Data Encryption standard
- ▪ Advanced encryption standard

### Detailed Notes
UNIT- 4
Modern
symmetric key ciphers

Unit-4
▪ Modern block ciphers
▪ Modern stream ciphers
▪ Data Encryption standard
▪ Advanced encryption standard
▪ Electronic Code Book Mode
▪ Cipher Block Chaining Mode
▪ Cipher Feedback Mode
▪ Output Feedback Mode

Lecture 19
Feistel Cipher

Round 1
Plaintext (2w bits)
F
w bitsw bits R0L0
K1
R1L1
Rn+1Ln+1
Round i
F
Ki
RiLi
Round n
F
Kn
Ln Rn
RnLn
Ciphertext (2w bits)
Feistel Cipher Structure
Or Block Cipher
Structure

Feistel Cipher Structure
▪ Input plaintext block of length 2w bits
▪ key K = n bits , Sub-keys: K1, K2, …, Kn (Derived from K)
▪ All rounds have the same structure.
▪ A substitution is performed by taking exclusive-OR on left half(Li)
of the data and the output of round function F which has inputs
right half(Ri) and sub key ki.
▪ A permutation is performed that consists of interchange of two
halves of data.
▪ This structure is called Substitution-Permutation Network (SPN)

Feistel Network Factors
▪ Block size: Common block size of 64-bit. However, the new
algorithms uses a 128-bit, 256-bit block size.
▪ Key size: Key sizes of 64 bits or less are now widely considered to
be insufficient, These days at least 128 bit, more better, e.g. 192
or 256 bit
▪ Number of rounds: A typical size is 16 rounds.
▪ Round function F: Again, greater complexity generally means
greater resistance to cryptanalysis.
▪ Subkey generation algorithm: Greater complexity in this
algorithm should lead to greater difficulty of cryptanalysis.

Feistel Encryption & Decryption
▪ Prove that o/p of first round
of Decryption is equal to 32-
bit swap of i/p of 16th round
of Encryption
▪ LD1=RE15 & RD1=LE15
▪ On Encryption Side:
▪ On Decryption Side:


### Extracted Images
![Lecture_19_16.9_Cryptography_BMK_p1_i0.png](assets/Lecture_19_16.9_Cryptography_BMK_p1_i0.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i0.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i0.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i1.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i1.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i2.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i2.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i3.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i3.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i4.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i4.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i5.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i5.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i6.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i6.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i7.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i7.png)

![Lecture_19_16.9_Cryptography_BMK_p7_i8.png](assets/Lecture_19_16.9_Cryptography_BMK_p7_i8.png)

---

## Lecture 1 22.7 Cryptography BMK

### Simple Notes (Key Points)
- ▪ Information Security understanding
- ▪ Security goals
- ▪ Security attacks
- ▪ Security Services
- ▪ Security Mechanism

### Detailed Notes
UNIT-1
Basics of
Cryptography

Outline
▪ Information Security understanding
▪ Security goals
▪ Security attacks
▪ Security Services
▪ Security Mechanism

Lecture 1
Information Security
Understanding

Introduction to Information & N/W Security

Security requirements tried

OSI Security Architecture
▪ The OSI (Open Systems Interconnection) security architecture
focuses on Security Attacks, Mechanisms, and Services.
▪ Security Attack: Any action that compromises the security of
information owned by an organization.
▪ Security Mechanism: A process that is designed to detect,
prevent, or recover from a security attack.
▪ Security Service: A communication service that enhances the
security of the data processing systems and the information
transfers of an organization.

Main Areas
▪ Symmetric encryption: Used to conceal the contents of blocks or
streams of data of any size, including messages, files, encryption
keys, and passwords.
▪ Asymmetric encryption: Used to conceal small blocks of data,
such as encryption keys and hash function values, which are used
in digital signatures.
▪ Data integrity algorithms: Used to protect blocks of data, such as
messages from alteration.
▪ Authentication Protocols: These are schemes based on the use of
cryptographic algorithms designed to authenticate the identity of
entities.


### Extracted Images
![Lecture_1_22.7_Cryptography_BMK_p1_i0.png](assets/Lecture_1_22.7_Cryptography_BMK_p1_i0.png)

![Lecture_1_22.7_Cryptography_BMK_p4_i0.jp2](assets/Lecture_1_22.7_Cryptography_BMK_p4_i0.jp2)

![Lecture_1_22.7_Cryptography_BMK_p5_i0.png](assets/Lecture_1_22.7_Cryptography_BMK_p5_i0.png)

---

## Lecture 20 17.9 Cryptography BMK

### Simple Notes (Key Points)
- Data Encryption Standard
- Data Encryption Standard (DES)
- ▪ Type: Block Cipher
- ▪ Key Size: 64-bit, with only 56-bit effective
- 64-bit plaintext 64-bit key

### Detailed Notes
Lecture 20
Data Encryption Standard

Data Encryption Standard (DES)
▪ Type: Block Cipher
▪ Block Size : 64-bit
▪ Key Size: 64-bit, with only 56-bit effective
▪ Number of Rounds: 16

Initial Permutation
Round 1
Round 2
Round 16
32-bit swap
Inverse
Initial Permutation
Permuted choice 2
Permuted choice 1
Left circular shift
Permuted choice 2 Left circular shift
Permuted choice 2 Left circular shift
64-bit plaintext 64-bit key
64-bit ciphertext
64 56
64
64
56
56
56
56
48K1
48K2
48K16
DES Encryption
Algorithm

Initial Permutation

Inverse
Initial Permutation

DES Encryption Algorithm (Cont…)
▪ First, the 64-bit plaintext passes through an initial permutation
(IP) that rearranges the bits to produce the permuted input.
▪ This is followed by a phase consisting of sixteen rounds of the
same function, which involves both permutation and substitution
functions.
▪ Finally, the preoutput is passed through a permutation that is the
inverse of the initial permutation function, to produce the 64-bit
ciphertext.
▪ The 56-bit key is passed through a permutation function.
▪ For each of the sixteen rounds, a subkey (Ki) is produced by the
combination of a left circular shift and a permutation.

DES Single Round

DES Single Round (Cont…)
1. Key Transformation
• Permutation of selection of sub-key from original key
2. Expansion Permutation (E-table)
• Right half is expanded from 32-bits to 48-bits
3. S-box Substitution
• Accepts 48-bits from XOR operation and produce 32-bits using
8 substitution boxes (each S-boxes has a 6-bit i/p and 4-bit
o/p).
4. P-Box Permutation
5. XOR and Swap

32-bits
32-bits
28-bits
28-bits
Expansion/ permutation
(E table)
XOR
Substitution/choice
(S-box)
Permutation
(P)
XOR
Left Shift
(S)
Left Shift
(S)
Permutation/
compression
(Permuted choice 2)
48
Ki
48
48
32
32

32-bits
32-bits
28-bits
28-bits
Expansion/ permutation
(E table)
XOR
Substitution/choice
(S-box)
Permutation
(P)
XOR
Left Shift
(S)
Left Shift
(S)
Permutation/
compression
(Permuted choice 2)
48
Ki
48
48
32
32

Role of S-box

Expansion Permutation

Role of S-box

Role of S-box (Cont…)
▪ The outer two bits of each group select one row of an S-box.
▪ Inner four bits selects one column of an S-box.
▪ Example:
S-box 1
0 1 1 0 0 1
Row Column
Input Output 1 0 0 1

Role of S-box

Permutation Function

32-bits
32-bits
28-bits
28-bits
Expansion/ permutation
(E table)
XOR
Substitution/choice
(S-box)
Permutation
(P)
XOR
Left Shift
(S)
Left Shift
(S)
Permutation/
compression
(Permuted choice 2)
48
Ki
48
48
32
32

Initial Permutation
Round 1
Round 2
Round 16
32-bit swap
Inverse
Initial Permutation
Permuted choice 2
Permuted choice 1
Left circular shift
Permuted choice 2 Left circular shift
Permuted choice 2 Left circular shift
64-bit plaintext 64-bit key
64-bit ciphertext
64 56
64
64
56
56
56
56
48K1
48K2
48K16
DES Encryption
Algorithm


### Extracted Images
![Lecture_20_17.9_Cryptography_BMK_p4_i0.jpg](assets/Lecture_20_17.9_Cryptography_BMK_p4_i0.jpg)

![Lecture_20_17.9_Cryptography_BMK_p4_i1.jpg](assets/Lecture_20_17.9_Cryptography_BMK_p4_i1.jpg)

![Lecture_20_17.9_Cryptography_BMK_p5_i0.jpg](assets/Lecture_20_17.9_Cryptography_BMK_p5_i0.jpg)

![Lecture_20_17.9_Cryptography_BMK_p7_i0.png](assets/Lecture_20_17.9_Cryptography_BMK_p7_i0.png)

![Lecture_20_17.9_Cryptography_BMK_p9_i0.png](assets/Lecture_20_17.9_Cryptography_BMK_p9_i0.png)

![Lecture_20_17.9_Cryptography_BMK_p9_i1.png](assets/Lecture_20_17.9_Cryptography_BMK_p9_i1.png)

![Lecture_20_17.9_Cryptography_BMK_p9_i2.png](assets/Lecture_20_17.9_Cryptography_BMK_p9_i2.png)

![Lecture_20_17.9_Cryptography_BMK_p9_i3.png](assets/Lecture_20_17.9_Cryptography_BMK_p9_i3.png)

![Lecture_20_17.9_Cryptography_BMK_p9_i4.png](assets/Lecture_20_17.9_Cryptography_BMK_p9_i4.png)

![Lecture_20_17.9_Cryptography_BMK_p9_i5.png](assets/Lecture_20_17.9_Cryptography_BMK_p9_i5.png)

![Lecture_20_17.9_Cryptography_BMK_p9_i6.png](assets/Lecture_20_17.9_Cryptography_BMK_p9_i6.png)

![Lecture_20_17.9_Cryptography_BMK_p9_i7.png](assets/Lecture_20_17.9_Cryptography_BMK_p9_i7.png)

![Lecture_20_17.9_Cryptography_BMK_p10_i0.png](assets/Lecture_20_17.9_Cryptography_BMK_p10_i0.png)

![Lecture_20_17.9_Cryptography_BMK_p10_i1.png](assets/Lecture_20_17.9_Cryptography_BMK_p10_i1.png)

![Lecture_20_17.9_Cryptography_BMK_p10_i2.png](assets/Lecture_20_17.9_Cryptography_BMK_p10_i2.png)

![Lecture_20_17.9_Cryptography_BMK_p10_i3.png](assets/Lecture_20_17.9_Cryptography_BMK_p10_i3.png)

![Lecture_20_17.9_Cryptography_BMK_p10_i4.png](assets/Lecture_20_17.9_Cryptography_BMK_p10_i4.png)

![Lecture_20_17.9_Cryptography_BMK_p10_i5.png](assets/Lecture_20_17.9_Cryptography_BMK_p10_i5.png)

![Lecture_20_17.9_Cryptography_BMK_p10_i6.png](assets/Lecture_20_17.9_Cryptography_BMK_p10_i6.png)

![Lecture_20_17.9_Cryptography_BMK_p10_i7.png](assets/Lecture_20_17.9_Cryptography_BMK_p10_i7.png)

![Lecture_20_17.9_Cryptography_BMK_p11_i0.png](assets/Lecture_20_17.9_Cryptography_BMK_p11_i0.png)

![Lecture_20_17.9_Cryptography_BMK_p12_i0.jpg](assets/Lecture_20_17.9_Cryptography_BMK_p12_i0.jpg)

![Lecture_20_17.9_Cryptography_BMK_p12_i1.jpg](assets/Lecture_20_17.9_Cryptography_BMK_p12_i1.jpg)

![Lecture_20_17.9_Cryptography_BMK_p13_i0.png](assets/Lecture_20_17.9_Cryptography_BMK_p13_i0.png)

![Lecture_20_17.9_Cryptography_BMK_p14_i0.png](assets/Lecture_20_17.9_Cryptography_BMK_p14_i0.png)

![Lecture_20_17.9_Cryptography_BMK_p15_i0.png](assets/Lecture_20_17.9_Cryptography_BMK_p15_i0.png)

![Lecture_20_17.9_Cryptography_BMK_p16_i0.jpg](assets/Lecture_20_17.9_Cryptography_BMK_p16_i0.jpg)

![Lecture_20_17.9_Cryptography_BMK_p17_i0.png](assets/Lecture_20_17.9_Cryptography_BMK_p17_i0.png)

![Lecture_20_17.9_Cryptography_BMK_p17_i1.png](assets/Lecture_20_17.9_Cryptography_BMK_p17_i1.png)

![Lecture_20_17.9_Cryptography_BMK_p17_i2.png](assets/Lecture_20_17.9_Cryptography_BMK_p17_i2.png)

![Lecture_20_17.9_Cryptography_BMK_p17_i3.png](assets/Lecture_20_17.9_Cryptography_BMK_p17_i3.png)

![Lecture_20_17.9_Cryptography_BMK_p17_i4.png](assets/Lecture_20_17.9_Cryptography_BMK_p17_i4.png)

![Lecture_20_17.9_Cryptography_BMK_p17_i5.png](assets/Lecture_20_17.9_Cryptography_BMK_p17_i5.png)

![Lecture_20_17.9_Cryptography_BMK_p17_i6.png](assets/Lecture_20_17.9_Cryptography_BMK_p17_i6.png)

![Lecture_20_17.9_Cryptography_BMK_p17_i7.png](assets/Lecture_20_17.9_Cryptography_BMK_p17_i7.png)

---

## Lecture 22 23.9 Cryptography BMK

### Simple Notes (Key Points)
- AES (Advance Encryption Standard)
- AES (Advanced Encryption Standard)
- Ciphertext (128 bits)
- Key (128-256 bits)
- 1. Expand 16-byte key to get

### Detailed Notes
Lecture 22
AES (Advance Encryption Standard)

AES (Advanced Encryption Standard)
AES
Plaintext (128 bits)
Ciphertext (128 bits)
Key (128-256 bits)

AES Structure
Initialization
1. Expand 16-byte key to get
the actual key block to be
used.
2. Initialize 16-byte plaintext
block called as state.
3. XOR the state with the key
block.
For each round
1. Apply S-box
2. Rotate rows of state
3. Mix columns
4. Add Round key: XOR the
state with key block.

AES (Advanced Encryption Standard)
▪ The Rijndael proposal for AES defined a cipher in which the block length
and the key length can be independently specified to be 128, 192, or
256 bits.
▪ AES designed to have characteristics
1. Resistance against all known attacks
2. Speed and code compactness on a wide range of platforms
3. Design simplicity
Key size 128 192 256
Plaintext Size 128 128 128
Round key 128 128 128
Number of Rounds 10 12 14

AES Overall Structure


### Extracted Images
![Lecture_22_23.9_Cryptography_BMK_p2_i0.png](assets/Lecture_22_23.9_Cryptography_BMK_p2_i0.png)

![Lecture_22_23.9_Cryptography_BMK_p2_i1.png](assets/Lecture_22_23.9_Cryptography_BMK_p2_i1.png)

![Lecture_22_23.9_Cryptography_BMK_p2_i2.png](assets/Lecture_22_23.9_Cryptography_BMK_p2_i2.png)

![Lecture_22_23.9_Cryptography_BMK_p2_i3.png](assets/Lecture_22_23.9_Cryptography_BMK_p2_i3.png)

![Lecture_22_23.9_Cryptography_BMK_p3_i0.jpg](assets/Lecture_22_23.9_Cryptography_BMK_p3_i0.jpg)

![Lecture_22_23.9_Cryptography_BMK_p5_i0.png](assets/Lecture_22_23.9_Cryptography_BMK_p5_i0.png)

---

## Lecture 23 24.9 Cryptography BMK

### Simple Notes (Key Points)
- Single Round AES & Key Scheduling
- AddRoundKey
- ▪ In the forward add round key transformation, the 128 bits of State
- are bitwise XORed with the 128 bits of the round key.
- State Round Key

### Detailed Notes
Lecture 23
Single Round AES & Key Scheduling

AES Overall Structure

Data Units in AES

Block to State & State to Block

Plain Text to State

Single AES Round

AES Structure
▪ The first N-1 rounds consist of four distinct transformation
functions.
• The 16 input bytes are substituted using an S-
boxSubBytes
• Each of the four rows of the matrix is shifted
to the leftShiftRows
• Each column of four bytes is now transformed
using a special mathematical function.MixColumns
• The 16 bytes of the matrix are now considered as
128 bits and are XORed to the 128 bits of the
round key.
AddRoundKe
y

SubByte Transformation
▪ The forward substitute byte transformation, called SubBytes, is a
simple table lookup



ShiftRows
▪ The first row of State is not altered.
▪ For the second row, a 1-byte circular left shift is performed.
▪ For the third row, a 2-byte circular left shift is performed.
▪ For the fourth row, a 3-byte circular left shift is performed.

MixColumns
▪ Each byte of a column is mapped into a new value that is a
function of all four bytes in that column.

AddRoundKey
▪ In the forward add round key transformation, the 128 bits of State
are bitwise XORed with the 128 bits of the round key.
State Round Key

AES Overall Structure

▪ The AES key expansion algorithm takes as
input a four-word (16-byte) key and produces
a linear array of 44 words (176 bytes).
▪ Each added word w[i] depends on the
immediately preceding word, w[i - 1].
▪ In three out of four cases, a simple XOR is
used.
AES Key Expansion

AES Key Expansion


### Extracted Images
![Lecture_23_24.9_Cryptography_BMK_p2_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p2_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p3_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p3_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p4_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p4_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p5_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p5_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p6_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p6_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p8_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p8_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p9_i0.jpg](assets/Lecture_23_24.9_Cryptography_BMK_p9_i0.jpg)

![Lecture_23_24.9_Cryptography_BMK_p10_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p10_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p10_i1.png](assets/Lecture_23_24.9_Cryptography_BMK_p10_i1.png)

![Lecture_23_24.9_Cryptography_BMK_p11_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p11_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p11_i1.png](assets/Lecture_23_24.9_Cryptography_BMK_p11_i1.png)

![Lecture_23_24.9_Cryptography_BMK_p12_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p12_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p13_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p13_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p14_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p14_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p15_i0.png](assets/Lecture_23_24.9_Cryptography_BMK_p15_i0.png)

![Lecture_23_24.9_Cryptography_BMK_p15_i1.png](assets/Lecture_23_24.9_Cryptography_BMK_p15_i1.png)

![Lecture_23_24.9_Cryptography_BMK_p15_i2.png](assets/Lecture_23_24.9_Cryptography_BMK_p15_i2.png)

---

## Lecture 24 26.9 Cryptography BMK

### Simple Notes (Key Points)
- Multiple Encryptions and Triple DES
- Double encryption
- Triple encryption
- Block Cipher Modes of Operations
- ▪ To apply a block cipher in a variety of applications, five "modes of

### Detailed Notes
Lecture 24
Multiple Encryptions and Triple DES

Double encryption
meet-in-the-middle attack

Triple encryption

Block Cipher Modes of Operations
▪ To apply a block cipher in a variety of applications, five "modes of
operation" have been defined.
▪ The five modes are intended to cover a wide variety of
applications of encryption for which a block cipher could be used.
▪ These modes are intended for use with any symmetric block
cipher, including triple DES and AES.
1. Electronic Code Book (ECB)
2. Cipher Block Chaining (CBC)
3. Cipher Feedback (CFB)
4. Output Feedback (OFB)
5. Counter (CTR)


### Extracted Images
![Lecture_24_26.9_Cryptography_BMK_p2_i0.png](assets/Lecture_24_26.9_Cryptography_BMK_p2_i0.png)

![Lecture_24_26.9_Cryptography_BMK_p2_i1.png](assets/Lecture_24_26.9_Cryptography_BMK_p2_i1.png)

![Lecture_24_26.9_Cryptography_BMK_p3_i0.png](assets/Lecture_24_26.9_Cryptography_BMK_p3_i0.png)

![Lecture_24_26.9_Cryptography_BMK_p3_i1.png](assets/Lecture_24_26.9_Cryptography_BMK_p3_i1.png)

---

## Lecture 25 30.9 Cryptography BMK

### Simple Notes (Key Points)
- Block Cipher Modes of Operations
- ▪ To apply a block cipher in a variety of applications, five "modes of
- operation" have been defined.
- applications of encryption for which a block cipher could be used.
- cipher, including triple DES and AES.

### Detailed Notes
Lecture 25
Block Chiper Modes

Block Cipher Modes of Operations
▪ To apply a block cipher in a variety of applications, five "modes of
operation" have been defined.
▪ The five modes are intended to cover a wide variety of
applications of encryption for which a block cipher could be used.
▪ These modes are intended for use with any symmetric block
cipher, including triple DES and AES.
1. Electronic Code Book (ECB)
2. Cipher Block Chaining (CBC)
3. Cipher Feedback (CFB)
4. Output Feedback (OFB)
5. Counter (CTR)

1. Electronic Code Book (ECB)
▪ In ECB Mode Plaintext handled one block at a time and each block
of plaintext is encrypted using the same key.
▪ The term codebook is used because, for a given key, there is a
unique ciphertext for every b-bit block of plaintext.

1. ECB Encryption & Decryption
P1
Encrypt
C1
K
P2
Encrypt
C2
K
PN
Encrypt
CN
K
C1
Decrypt
P1
K
C2
Decrypt
P2
K
CN
Decrypt
PN
K
64-bit 64-bit 64-bit
64-bit 64-bit 64-bit
64-bit 64-bit 64-bit
64-bit 64-bit 64-bit

Electronic Code Book - Cont…
▪ Strength: it’ssimple.
▪ Weakness:
o Repetitive information contained in the plaintext may show in
the ciphertext, if aligned with blocks.
o If the message has repetitive elements with a period of
repetition a multiple of b bits, then these elements can be
identified by the analyst.
▪ Typical application:
o Secure transmission of short pieces of information (e.g. a
temporary encryption key)

2. Cipher Block Chaining (CBC)
▪ CBC is a technique in which the same plaintext block, if repeated,
produces different ciphertext blocks.
▪ In this scheme, the input to the encryption algorithm is the XOR of
the current plaintext block and the preceding ciphertext block; the
same key is used for each block.
▪ To produce the first block of ciphertext, an initialization vector
(IV) is XORed with the first block of plaintext.
▪ On decryption, the IV is XORed with the output of the decryption
algorithm to recover the first block of plaintext.

2. CBC - Encryption & Decryption
P1
Encrypt
C1
K
IV
P2
Encrypt
C2
K
PN
Encrypt
CN
K
C1
Decrypt
P1
K
IV
C2
Decrypt
P2
K
CN
Decrypt
PN
K
CN-1
CN-1

2. Cipher Block Chaining (CBC) –Cont…
▪ Strength: because of the chaining mechanism of CBC, it is an
appropriate mode for encrypting messages of length greater than
b bits
▪ Typical application:
o General-purpose block oriented transmission
o Authentication

3. Cipher Feedback Mode (CFB)
▪ For AES, DES, or any block cipher, encryption is performed on a
block of b bits. In DES, b = 64 and in AES, b = 128.
▪ However, it is possible to convert a block cipher into a stream
cipher, using cipher feedback (CFB) mode, output feedback (OFB)
mode, and counter (CTR) mode.
▪ A stream cipher eliminates the need to pad a message to be an
integral number of blocks.

IV
Encrypt
K
Select
s bits
Discard
b-s bits
P1
S bits
C1
S bits
Shift register
b-s bits | s bits
Encrypt
K
Select
s bits
Discard
b-s bits
P2
S bits
C2
S bits
Shift register
b-s bits | s bits
Encrypt
K
Select
s bits
Discard
b-s bits
PN
S bits
CN
S bits
CN-1
3. CFB Encryption

IV
Encrypt
K
Select
s bits
Discard
b-s bits
P1
S bits
Shift register
b-s bits | s bits
Encrypt
K
Select
s bits
Discard
b-s bits
P2
S bits
Shift register
b-s bits | s bits
Encrypt
K
Select
s bits
Discard
b-s bits
PN
S bits
CN-1
3. CFB Decryption
CN
S bits
C2
S bits
C1
S bits

CFB Mode
▪ The input to the encryption function is a b-bit shift register that is
initially set to some initialization vector (IV).
▪ The leftmost (most significant) s bits of the output of the
encryption function are XORed with the first segment of plaintext
P1 to produce the first unit of ciphertext C1 , which is then
transmitted.
▪ In addition, the contents of the shift register are shifted left by s
bits, and C1 is placed in the rightmost (least significant) s bits of
the shift register.
▪ For decryption, the same scheme is used, except that the received
ciphertext unit is XORed with the output of the encryption
function to produce the plaintext unit.

CFB Mode –Cont…

4. Output Feedback Mode (OFB)
▪ The output feedback (OFB) mode is similar in structure to that of
CFB.
▪ For OFB, the output of the encryption function is fed back to
become the input for encrypting the next block of plaintext.
▪ In CFB, the output of the XOR unit is fed back to become input for
encrypting the next block.
▪ The other difference is that the OFB mode operates on full blocks
of plaintext and ciphertext, whereas CFB operates on an s-bit
subset.
▪ Nonce: A time-varying value that has at most a negligible chance
of repeating, for example, a random value that is generated anew
for each use, a timestamp, a sequence number, or some
combination of these.

Nonce
Encrypt
C1
K
P1
4. OFB Encryption
Encrypt
C2
K
P2
Encrypt
CN
K
PN

Nonce
Encrypt
P1
K
C1
4. OFB Decryption
Encrypt
P2
K
C2
Encrypt
PN
K
CN

OFB Mode
▪ Each bit in the ciphertext is independent of the previous bit or
bits.
▪ This avoids error propagation
▪ Pre-compute of forward cipher is possible

Counter (CTR) Mode

Counter (CTR) Mode


### Extracted Images
![Lecture_25_30.9_Cryptography_BMK_p8_i0.png](assets/Lecture_25_30.9_Cryptography_BMK_p8_i0.png)

![Lecture_25_30.9_Cryptography_BMK_p13_i0.png](assets/Lecture_25_30.9_Cryptography_BMK_p13_i0.png)

![Lecture_25_30.9_Cryptography_BMK_p17_i0.png](assets/Lecture_25_30.9_Cryptography_BMK_p17_i0.png)

![Lecture_25_30.9_Cryptography_BMK_p18_i0.png](assets/Lecture_25_30.9_Cryptography_BMK_p18_i0.png)

![Lecture_25_30.9_Cryptography_BMK_p19_i0.png](assets/Lecture_25_30.9_Cryptography_BMK_p19_i0.png)

---

## Lecture 26 3.10 Cryptography BMK

### Simple Notes (Key Points)
- Asymmetric Encryption and RSA
- ▪ Key Management
- ▪ Diffie-Hillman Key Exchange algorithm
- Symmetric key Encryption
- Encryption Algorithm

### Detailed Notes
UNIT-5
Public key
cryptography

Lecture 26
Asymmetric Encryption and RSA

Outline
▪ RSA
▪ RSA proof with example
▪ RSA attacks
▪ Rabin cryptosystem
▪ Key Management
▪ Diffie-Hillman Key Exchange algorithm

Symmetric key Encryption
Plaintext
input
Plaintext
output
Encryption Algorithm
(e.g. AES)
Decryption Algorithm
(reverse of encryption
algorithm)
Secret key shared by
sender and recipient
X
Secret key shared by
sender and recipient
K
Transmitted
cipher text
Y = E(K, X)
K
X

Plaintext
input
Plaintext
outputEncryption Algorithm
(e.g. RSA)
Decryption Algorithm
X
Transmitted
cipher text
Y = E(PUa, X)
X
Bob’s
Public
key ring
Alice
Ted
Mike
Joy
Alice’s public
key
PUa Alice’s private
key
PRa
Asymmetric key Encryption with Public Key
Bob Alice
▪ The entire encrypted message
serves as a confidentiality.

Plaintext
input
Plaintext
outputEncryption Algorithm
(e.g. RSA)
Decryption Algorithm
X
Transmitted
cipher text
Y = E(PRb, X)
X
Alice’s
Public
key ring
Bob
Ted
Mike
Joy
Bob’s public
key
PUbBob’s private
key
PRb
Asymmetric key Encryption with Private Key
Bob Alice
▪ The entire encrypted message
serves as a digital signature.

Authentication and Confidentiality
Message
source
Encryption
Algorithm
Encryption
Algorithm
Decryption
Algorithm
Decryption
Algorithm
Message
Dest.
X Y Y XZ
Key pair
source
Key pair
sourcePRa PUa
PRbPUb
Source A Source B
Z = E(PUb, E(PRa, X)) X = D(PUa, D(PRB, Z))

Applications for Public-Key Cryptosystems
▪ Encryption/decryption: The sender encrypts a message with the
recipient’spublic key.
▪ Digital signature: The sender “signs” a message with its private
key. Signing is achieved by a cryptographic algorithm applied to
the message or to a small block of data that is a function of the
message.
▪ Key exchange: Two sides cooperate to exchange a session key.
Several different approaches are possible, involving the private
key(s) of one or both parties.

RSA Algorithm
▪ RSA is a block cipher in which the Plaintext and Ciphertext are
represented as integers between 0 and n-1 for some n.
▪ Large messages can be broken up into a number of blocks.
▪ Each block would then be represented by an integer.
Step-1: Generate Public key and Private key
Step-2: Encrypt message using Public key
Step-3: Decrypt message using Private key

Step-1: Generate Public key and Private key
▪ Select two large prime numbers: p and q
▪ Calculate modulus : n = p * q
▪ Calculate Euler’stotient function : φ(n) = (p-1) * (q-1)
▪ Select e such that e is relatively prime to φ(n) and 1 < e < φ(n)
▪ Determine d such that d * e ≡ 1 (mod φ(n))
▪ Publickey : PU = { e, n }
▪ Privatekey : PR = { d, n }
Two numbers are relatively prime if they have no common factors
other than 1.

Step-2 : Encrypt Message
▪ Encryption Using Public key: C = Me mod n
Ciphertext Input
Message
Publickey
PU = { e, n }

Step-3 : Decrypt Message
▪ Encryption Using Public key: M = Cd mod n
Plaintext
Message
Cipher
Message
Privatekey
PR = { d, n }


### Extracted Images
![Lecture_26_3.10_Cryptography_BMK_p1_i0.png](assets/Lecture_26_3.10_Cryptography_BMK_p1_i0.png)

![Lecture_26_3.10_Cryptography_BMK_p4_i0.png](assets/Lecture_26_3.10_Cryptography_BMK_p4_i0.png)

![Lecture_26_3.10_Cryptography_BMK_p4_i1.png](assets/Lecture_26_3.10_Cryptography_BMK_p4_i1.png)

![Lecture_26_3.10_Cryptography_BMK_p4_i2.png](assets/Lecture_26_3.10_Cryptography_BMK_p4_i2.png)

![Lecture_26_3.10_Cryptography_BMK_p5_i0.png](assets/Lecture_26_3.10_Cryptography_BMK_p5_i0.png)

![Lecture_26_3.10_Cryptography_BMK_p5_i1.png](assets/Lecture_26_3.10_Cryptography_BMK_p5_i1.png)

![Lecture_26_3.10_Cryptography_BMK_p5_i2.png](assets/Lecture_26_3.10_Cryptography_BMK_p5_i2.png)

![Lecture_26_3.10_Cryptography_BMK_p6_i0.png](assets/Lecture_26_3.10_Cryptography_BMK_p6_i0.png)

![Lecture_26_3.10_Cryptography_BMK_p6_i1.png](assets/Lecture_26_3.10_Cryptography_BMK_p6_i1.png)

![Lecture_26_3.10_Cryptography_BMK_p6_i2.png](assets/Lecture_26_3.10_Cryptography_BMK_p6_i2.png)

---

## Lecture 27 7.10 Cryptography BMK

### Simple Notes (Key Points)
- Step-1: Generate Public key and Private key
- ▪ Public key : PU = { e, n } , PU = { 7, 33 }
- ▪ Private key : PR = { d, n }, PR = { 3, 33 }
- ▪ Encryption Using Public key: C = Me mod n
- Ciphertext Input

### Detailed Notes
Lecture 27
RSA proof with example

Step-1: Generate Public key and Private key
▪ Select two large prime numbers: p = 3 and q = 11
▪ Calculate modulus : n = p * q, n = 33
▪ Calculate Euler’s totient function : φ(n)= (p-1) * (q-1)
φ(n)= ( 3 –1 ) * ( 11 –1 ) = 20
▪ Select e such that e is relatively prime to φ(n)and 1 < e < φ(n)
▪ We have several choices for e : 7, 11, 13, 17, 19 Let’s take e = 7
▪ Determine d such that d * e ≡1 (mod φ(n))
▪ ? * 7 ≡1 (mod 20)
▪ 3 * 7 ≡1 (mod 20)
▪ Public key : PU = { e, n } , PU = { 7, 33 }
▪ Private key : PR = { d, n }, PR = { 3, 33 }
•This is equivalent to
finding d which satisfies
de = 1 + j.φ(n) where j is
any integer.
•We can rewrite this as
d = (1 + j. φ(n)) / e

Step-2 : Encrypt Message
▪ Encryption Using Public key: C = Me mod n
Ciphertext Input
Message
Publickey
For message M = 14
C = 147 mod 33
C = [(141 mod 33) X (142 mod 33) X (144 mod 33)] mod 33
C = (14 X 31 X 4) mod 33 = 1736 mod 33
C = 20
PU = { e, n } , PU = { 7, 33 }

Step-3 : Decrypt Message
▪ Encryption Using Public key: M = Cd mod n
Plaintext
Message
Cipher
Message
Privatekey
For Ciphertext C = 20
M = 203 mod 33
M = [(201 mod 33) X (202 mod 33)] mod 33
M = (20 X 4) mod 33 = 80 mod 33
M = 14
PR = { d, n } , PR = { 3, 33 }

Example RSA Algorithm
147 mod 33 = 20 Plaintext
14
Plaintext
14203 mod 33 = 14 Ciphertext
20
PU = 7, 33 PR = 3, 33
Encryption Decryption

RSA Example
▪ Find n, φ(n), e, d for p=7 and q= 19 then demonstrate encryption
and decryption for M = 6
n = p * q = 7 * 19 = 133
φ(n) = ( p – 1 ) * ( q – 1) = 108
Finding e relatively prime to 108
e = 2 => GCD( 2, 108 ) = 2 (no)
e = 3 => GCD( 3, 108 ) = 3 (no)
e = 5 => GCD( 5, 108 ) = 1 (Yes)
• Finding d such that (d * e ) mod φ(n) = 1
• We can rewrite this as d = (1 + j . φ(n)) /
e
j = 0  => d = 1 / 5 = 0.2 🡨integer ? (no)
j = 1  => d = 109 / 5 = 21.8 🡨integer ? (no)
j = 2  => d = 217 / 5 = 43.4 🡨integer ? (no)
j = 3  => d = 325 / 5 = 65 integer ? (yes)
Public key :
PU = { e, n } = {5, 133}
Private key :
PR = { d, n } = {65, 133}

RSA Example – cont…
▪ Encryption:
C = Me mod n
For message M = 6
C = 65 mod 133
C = 7776 mod 33
C = 62
PU = { e, n } , PU = { 5, 133 }
▪ Decryption:
M = Cd mod n
For C = 62
M = 6265 mod 133
M = 2666 mod 33
M = 6
PR = { d, n } , PU = { 65, 133 }

RSA Example
▪ P and Q are two prime numbers. P=7, and Q=17. Take public key
E=5. If plain text value is 10, then what will be cipher text value
according to RSA algorithm?
▪ n = 119
▪ φ(n) = 96
▪ e = 5
▪ d = 77
▪ PU = { 5, 119 }
▪ PR = {77, 119}
▪ C = 105 mod 119 => C = 40


---

## Lecture 28 8.10 Cryptography BMK

### Simple Notes (Key Points)
- Diffie-Hellman key Exchange
- Diffie-Hellman key Exchange
- ▪ The purpose of the Diffie-Hellman algorithm is to enable two
- users to securely exchange a key that can be used for subsequent
- encryption of message.

### Detailed Notes
Lecture 28
Diffie-Hellman key Exchange

Diffie-Hellman key Exchange
▪ The purpose of the Diffie-Hellman algorithm is to enable two
users to securely exchange a key that can be used for subsequent
encryption of message.
▪ This algorithm depends for its effectiveness on the difficulty of
computing discrete logarithms.

Primitive root

Discrete Logarithm

Diffie-Hellman Key Exchange –Cont…

Diffie-Hellman Key Exchange –Cont…

Diffie-Hellman Key Exchange –Cont…

Diffie-Hellman Key Exchange –Cont…



Diffie-Hellman Key Exchange Example

Diffie-Hellman Key Exchange Illustration


### Extracted Images
![Lecture_28_8.10_Cryptography_BMK_p3_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p3_i0.png)

![Lecture_28_8.10_Cryptography_BMK_p3_i1.png](assets/Lecture_28_8.10_Cryptography_BMK_p3_i1.png)

![Lecture_28_8.10_Cryptography_BMK_p3_i2.png](assets/Lecture_28_8.10_Cryptography_BMK_p3_i2.png)

![Lecture_28_8.10_Cryptography_BMK_p4_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p4_i0.png)

![Lecture_28_8.10_Cryptography_BMK_p4_i1.png](assets/Lecture_28_8.10_Cryptography_BMK_p4_i1.png)

![Lecture_28_8.10_Cryptography_BMK_p4_i2.png](assets/Lecture_28_8.10_Cryptography_BMK_p4_i2.png)

![Lecture_28_8.10_Cryptography_BMK_p5_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p5_i0.png)

![Lecture_28_8.10_Cryptography_BMK_p6_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p6_i0.png)

![Lecture_28_8.10_Cryptography_BMK_p6_i1.png](assets/Lecture_28_8.10_Cryptography_BMK_p6_i1.png)

![Lecture_28_8.10_Cryptography_BMK_p6_i2.png](assets/Lecture_28_8.10_Cryptography_BMK_p6_i2.png)

![Lecture_28_8.10_Cryptography_BMK_p7_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p7_i0.png)

![Lecture_28_8.10_Cryptography_BMK_p7_i1.png](assets/Lecture_28_8.10_Cryptography_BMK_p7_i1.png)

![Lecture_28_8.10_Cryptography_BMK_p7_i2.png](assets/Lecture_28_8.10_Cryptography_BMK_p7_i2.png)

![Lecture_28_8.10_Cryptography_BMK_p7_i3.png](assets/Lecture_28_8.10_Cryptography_BMK_p7_i3.png)

![Lecture_28_8.10_Cryptography_BMK_p8_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p8_i0.png)

![Lecture_28_8.10_Cryptography_BMK_p8_i1.png](assets/Lecture_28_8.10_Cryptography_BMK_p8_i1.png)

![Lecture_28_8.10_Cryptography_BMK_p9_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p9_i0.png)

![Lecture_28_8.10_Cryptography_BMK_p10_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p10_i0.png)

![Lecture_28_8.10_Cryptography_BMK_p11_i0.png](assets/Lecture_28_8.10_Cryptography_BMK_p11_i0.png)

---

## Lecture 29 15.10 Cryptography BMK

### Simple Notes (Key Points)
- Step-1: Generate Public key and Private key
- ▪ Public key : PU = { n } , PU = { 77 }
- ▪ Private key : PR = { p, q }, PR = { 7, 11 }

### Detailed Notes
Lecture 29
Rabin cryptosystem

Step-1: Generate Public key and Private key
▪ Select two large prime numbers: p = 7 and q = 11
▪ Calculate modulus : n = p * q, n = 77
▪ Public key : PU = { n } , PU = { 77 }
▪ Private key : PR = { p, q }, PR = { 7, 11 }

Step-2 : Encrypt Message
C = M2 mod n
For message M = 5 (0 < M < n)
C = 52 mod 77
C = 25 mod 77
C = 25
PU = { n } , PU = { 77 }

Step-3 : Decrypt Message
Mp = C(p+1)/4 mod p
Mp = 25(7+1)/4 mod 7
Mp = 252 mod 7
Mp = 625 mod 7
Mp = 2
Mq = C(q+1)/4 mod q
Mq = 25(11+1)/4 mod 7
Mq = 253 mod 7
Mq ≡ 33 mod 7
Mq = 5
Calculate Roots Modulo p and q

Step-3 : Decrypt Message
Determine the Four Plaintext Candidates
M ≡+Mp​(modp) and M≡+Mq​(modq)
M ≡+Mp​(modp) and M≡−Mq​(modq)
M ≡−Mp​(modp) and M≡+Mq​(modq)
M ≡−Mp​(modp) and M≡−Mq​(modq)
(Finding the Four Plaintexts M1​,M2​,M3​,M4​ for C=25):
We have p=7, q=11, n=77, Mp​=2, Mq​=5. The roots are:
• ±Mp ​mod7→2 and 7−2=5
• ±Mq ​mod11→5 and 11−5=6

Step-3 : Decrypt Message
Determine the Four Plaintext Candidates
Pair Congruences
Chinese Remainder
Theorem Solution Result
P1
M≡2(mod7) and
M≡5(mod11) Solved for M M1​=16
P2
M≡2(mod7) and
M≡6(mod11) Solved for M M2​=72
P3
M≡5(mod7) and
M≡5(mod11) Solved for M
M3​=5 (The original
message)
P4
M≡5(mod7) and
M≡6(mod11) Solved for M M4​=61


### Extracted Images
![Lecture_29_15.10_Cryptography_BMK_p5_i0.png](assets/Lecture_29_15.10_Cryptography_BMK_p5_i0.png)

![Lecture_29_15.10_Cryptography_BMK_p5_i1.png](assets/Lecture_29_15.10_Cryptography_BMK_p5_i1.png)

---

## Lecture 30 04.11 Cryptography BMK

### Simple Notes (Key Points)
- ▪ Security of Hash functions
- Key Properties of cryptographic hash function

### Detailed Notes
UNIT-6
Message
Authentication
& Hash Function

Outline
▪ Authentication requirements
▪ Functions
▪ Message authentication codes (MAC)
▪ Hash functions .
▪ Security of Hash functions

Lecture 30
Authentication Requirements

Message Authentication
▪ Message authentication is a procedure to verify that received
messages come from the genuine source and have not been
altered.
▪ Message authentication may also verify sequencing and
timeliness.
▪ Message authentication is a mechanism or service used to verify
the integrity of  a message.
▪ Message authentication assures that data received are exactly as
sent (i.e., contain no modification, insertion, deletion, or replay).

Message Authentication Requirements
1. Disclosure: Release of message contents
2. Traffic analysis: Discovery of the pattern of traffic between
parties
3. Masquerade: Insertion of messages into the network from a
fraudulent source
4. Content modification: Changes to the contents of a message
5. Sequence modification: Any modification to a sequence of
messages between parties
6. Timing modification: Delay or replay of messages
7. Source repudiation: Denial of transmission of message by source
8. Destination repudiation: Denial of receipt of message by
destination

INS is very Interesting Subject
Message Authentication Requirements
1. Disclosure
2. Traffic analysis
3. Masquerade
4. Content modification
5. Sequence modification
6. Timing modification
7. Source repudiation
8. Destination repudiation
Requires Message
Confidentiality
Requires Message
Authentication
Requires Digital
Signature

















Cryptographic Hash Function
h = H(M)

Key Properties of cryptographic hash function
Deterministic
Computationally infeasible
Collision Resistance
Avalanche Effect
Application of cryptographic hash function
Message Authentication Codes (MACs)
Digital signatures
Data integrity verification
Password storage (hashed passwords)
Blockchain and cryptocurrency


### Extracted Images
![Lecture_30_04.11_Cryptography_BMK_p1_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p1_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p7_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p7_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p8_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p8_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p9_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p9_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p10_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p10_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p11_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p11_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p12_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p12_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p13_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p13_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p14_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p14_i0.png)

![Lecture_30_04.11_Cryptography_BMK_p15_i0.png](assets/Lecture_30_04.11_Cryptography_BMK_p15_i0.png)

---

## Lecture 31 07.11 Cryptography BMK

### Simple Notes (Key Points)
- Message encryption
- The ciphertext of the entire message serves as its authenticator
- A function of the message and a secret key that produces a fixed-
- Both Source A and Destination B share the same secret key (K).
- A encrypts the message M using this key:

### Detailed Notes
Lecture 31
Message Authentication Code

Hash Function
Message Authentication Function
A function that maps a message of any length into a fixed length
hash value, which serves as the authenticator
Message encryption
The ciphertext of the entire message serves as its authenticator
Message authentication code
A function of the message and a secret key that produces a fixed-
length value that serves as the authenticator



Process:
Both Source A and Destination B share the same secret key (K).
A encrypts the message M using this key:
𝐶 = 𝐸 𝐾 𝑀
B decrypts it using the same key K:
𝑀 = 𝐷 𝐾 𝐶
Features:
Confidentiality: Only A and B know the secret key, so others cannot read the message.
Authentication: Since only A and B know K, B can be sure that the message came from A.
Drawback: Managing and securely sharing secret keys between multiple users is difficult.

Process:
Destination B has a public/private key pair (PUb, PRb).
Source A encrypts the message with B’s public key:
𝐶 = 𝐸(𝑃𝑈𝑏, 𝑀)
B decrypts it with their private key:
𝑀 = 𝐷(𝑃𝑅𝑏, 𝐶)
Features:
Confidentiality: Only B can decrypt because only B knows PRb.
No Authentication: Anyone can use B’s public key to send messages,
so B can’t be sure who sent it.

Process:
Source A has a public/private key pair (PUa, PRa).
A encrypts the message using their private key:
𝐶 = 𝐸(𝑃𝑅𝑎, 𝑀)
B decrypts it using A’s public key:
𝑀 = 𝐷(𝑃𝑈𝑎, 𝐶)
Features:
Authentication: Since only A knows PRa, successful decryption with PUa proves the
message is from A.
Digital Signature: It also acts as a signature, verifying A’s identity.
No Confidentiality: Anyone can decrypt using PUa (public key).

Process:
Combines both (b) and (c):
A first encrypts the message using their private key (PRa) → provides authentication.
𝐸(𝑃𝑅𝑎, 𝑀)
Then encrypts that result using B’s public key (PUb) → provides confidentiality.
𝐸(𝑃𝑈𝑏, 𝐸 𝑃𝑅𝑎, 𝑀 )
B decrypts first using their private key (PRb), then using A’s public key (PUa):
𝑀 = 𝐷 𝑃 𝑈𝑎𝐷 𝑃 𝑅𝑏𝐶
Features:
Confidentiality: Only B can decrypt the outer layer (PUb/PRb).
Authentication & Signature: Decryption with PUa confirms it was sent by A.
Integrity: Any modification to the message will be detected because decryption will fail.

Message Authentication Code
▪ An alternative authentication technique involves the use of a secret key to generate a
small fixed-size block of data, known as a cryptographic checksum or MAC
▪ MAC is appended to the message. This technique assumes that two communicating
parties, say A and B, share a common secret key K.
▪ When A has a message to send to B, it calculates the MAC as a function of the message
and the key
MAC = C ( K , M )
Purpose
Integrity → ensures the message was not altered during transmission.
Authentication → ensures the message really came from the sender who knows the secret key.

Message Authentication Code
Purpose
Integrity → ensures the message was not altered during transmission.
Authentication → ensures the message really came from the sender who knows the secret key.
How it works
Both sender (A) and receiver (B) share a secret key K.
A uses a MAC function 𝐶to compute:
𝑀𝐴𝐶 = 𝐶 𝐾 𝑀
Then A sends both the message M and the MAC to B.
B uses the same secret key 𝐾to compute its own MAC for the received message and
compares it with the received MAC.
If both match → message is authentic and unmodified.

Message Authentication Code
Process
1. Source A computes: 𝐶 𝐾 𝑀
2. A sends both 𝑀and 𝐶 𝐾 𝑀 to B.
3. B recomputes 𝐶 𝐾 𝑀 using the same key 𝐾and compares it.
Purpose
Authenticity: Only someone with key 𝐾can generate the correct MAC.
Integrity: If message changes, MAC comparison fails.
No Confidentiality: Message 𝑀is sent in plaintext.

Two keys are used:
𝐾1 :For MAC generation. 𝐾2 :For encryption/decryption.
Process
Compute MAC:
𝐶 𝐾1 𝑀
Concatenate message and MAC:
𝑀 ∣∣ 𝐶 𝐾1 𝑀
Encrypt the entire block:
𝐸 𝐾2 𝑀 ∣∣ 𝐶 𝐾1 𝑀
Send to destination.
Destination decrypts → verifies MAC.
Purpose
Confidentiality (via encryption with 𝐾2)
Authentication & Integrity (via MAC with 𝐾1)
MAC is tied to plaintext because MAC is computed before encryption.

INS is very Interesting Subject
Two keys again:
𝐾2 :For encryption/decryption. 𝐾1 :For MAC computation.
Process
Encrypt the message:
𝐸 𝐾2 𝑀
Compute MAC over the ciphertext:
𝐶 𝐾1 𝐸 𝐾2 𝑀
Send both:
𝐸 𝐾2 𝑀 ∣∣ 𝐶 𝐾1 𝐸 𝐾2 𝑀
Receiver verifies MAC first, then decrypts.
Purpose
Confidentiality: via encryption (same as before).
Authentication: via MAC on ciphertext (any tampering with ciphertext is detected before
decryption).
MAC is tied to ciphertext, giving extra protection against attacks that try to alter the
ciphertext directly.

INS is very Interesting Subject
Case Process Keys Used Confidentiality Authentication MAC Tied
To
(a) Plaintext +
MAC K
Plaintext
(b) Encrypt
[M‖MAC] K₁, K₂
Plaintext
(c) MAC over
ciphertext K₁, K₂
Ciphertext

Message Authentication code - Cont…
▪ The receiver is assured that the message is from the alleged
sender.
▪ Because no one else knows the secret key, no one else could
prepare a message with a proper MAC.
▪ A MAC function is similar to encryption. One difference is that the
MAC algorithm need not be reversible, as it must be for
decryption.
▪ In general, the MAC function is a many-to-one function. The
domain of the function consists of messages of some arbitrary
length, whereas the range consists of all possible MACs and all
possible keys.
▪ If an n-bit MAC is used, then there are 2 n  possible MACs


### Extracted Images
![Lecture_31_07.11_Cryptography_BMK_p3_i0.jpg](assets/Lecture_31_07.11_Cryptography_BMK_p3_i0.jpg)

![Lecture_31_07.11_Cryptography_BMK_p4_i0.png](assets/Lecture_31_07.11_Cryptography_BMK_p4_i0.png)

![Lecture_31_07.11_Cryptography_BMK_p5_i0.png](assets/Lecture_31_07.11_Cryptography_BMK_p5_i0.png)

![Lecture_31_07.11_Cryptography_BMK_p5_i1.png](assets/Lecture_31_07.11_Cryptography_BMK_p5_i1.png)

![Lecture_31_07.11_Cryptography_BMK_p6_i0.png](assets/Lecture_31_07.11_Cryptography_BMK_p6_i0.png)

![Lecture_31_07.11_Cryptography_BMK_p6_i1.png](assets/Lecture_31_07.11_Cryptography_BMK_p6_i1.png)

![Lecture_31_07.11_Cryptography_BMK_p7_i0.png](assets/Lecture_31_07.11_Cryptography_BMK_p7_i0.png)

![Lecture_31_07.11_Cryptography_BMK_p7_i1.png](assets/Lecture_31_07.11_Cryptography_BMK_p7_i1.png)

![Lecture_31_07.11_Cryptography_BMK_p10_i0.png](assets/Lecture_31_07.11_Cryptography_BMK_p10_i0.png)

![Lecture_31_07.11_Cryptography_BMK_p11_i0.png](assets/Lecture_31_07.11_Cryptography_BMK_p11_i0.png)

![Lecture_31_07.11_Cryptography_BMK_p11_i1.png](assets/Lecture_31_07.11_Cryptography_BMK_p11_i1.png)

![Lecture_31_07.11_Cryptography_BMK_p12_i0.png](assets/Lecture_31_07.11_Cryptography_BMK_p12_i0.png)

![Lecture_31_07.11_Cryptography_BMK_p12_i1.png](assets/Lecture_31_07.11_Cryptography_BMK_p12_i1.png)

![Lecture_31_07.11_Cryptography_BMK_p13_i0.png](assets/Lecture_31_07.11_Cryptography_BMK_p13_i0.png)

![Lecture_31_07.11_Cryptography_BMK_p13_i1.png](assets/Lecture_31_07.11_Cryptography_BMK_p13_i1.png)

![Lecture_31_07.11_Cryptography_BMK_p13_i2.png](assets/Lecture_31_07.11_Cryptography_BMK_p13_i2.png)

![Lecture_31_07.11_Cryptography_BMK_p13_i3.png](assets/Lecture_31_07.11_Cryptography_BMK_p13_i3.png)

---

## Lecture 33 19.11 Cryptography BMK

### Simple Notes (Key Points)
- Hash Algorithms
- ▪ Hash Algorithms
- Symmetric-key
- • Block ciphers
- • Stream ciphers

### Detailed Notes
UNIT-7
Hash Algorithms
Digital Signature

Lecture 33
Digital Signature

Outline
▪ Digital Signatures
▪ Hash Algorithms

Symmetric-key
ciphers:
• Block ciphers
• Stream ciphers
Public-key
ciphers
Cryptographic Goals
Cryptographic goals
Confidentiality Data integrity Authentication Non-repudiation
Message authentication
Entity authenticationArbitrary length
hash functions
Message
Authentication
codes (MACs)
Digital signatures
Authentication
primitives
Digital signatures
• MACs
• Digital
signatures

Digital Signature
▪ A digital signature is an authentication mechanism that enables
the creator of a message to attach a code that acts as a signature.
▪ Typically the signature is formed by taking the hash of the
message and encrypting the message with the creator’s private
key.
▪ The signature guarantees the source and integrity of the message.
▪ The digital signature standard (DSS) is an NIST standard that uses
the secure hash algorithm (SHA).



Hash code, MAC and Digital Signature
Hash Code
▪ A hash of the message, if appended to the message itself, only
protects against accidental changes to the message, as an attacker
who modifies the message can simply calculate a new hash and
use it instead of the original one. So this only gives integrity.
MAC
▪ A message authentication code (MAC) (sometimes also known as
keyed hash) protects against message forgery by anyone who
doesn't know the secret.
▪ This means that the receiver can forge any message – thus we
have both integrity and authentication (as long as the receiver
doesn't have a split personality), but not non-repudiation.

Hash code, MAC and Digital Signature
Digital Signature
▪ A digital signature is created with a private key, and verified with
the corresponding public key of an asymmetric key-pair.
▪ Only the holder of the private key can create this signature, and
normally anyone knowing the public key can verify it.

Attacks and Forgeries
▪ Key-only attack: C only knows A’s public key.
▪ Known message attack: C is given access to a set of messages and their
signatures.
▪ Generic chosen message attack: C chooses a list of messages before
attempting to breaks A’s signature scheme, independent of A’s public
key. C then obtains from A valid signatures for the chosen messages. The
attack is generic, because it does not depend on A’s public key; the same
attack is used against everyone.
▪ Directed chosen message attack: Similar to the generic attack, except
that the list of messages to be signed is chosen after C knows A’s public
key but before any signatures are seen.
▪ Adaptive chosen message attack: C is allowed to use A as an “oracle.”
This means the A may request signatures of messages that depend on
previously obtained message–signature pairs.

Attacks and Forgeries
▪ Total break: C determines A’s private key.
▪ Universal forgery: C finds an efficient signing algorithm that provides an
equivalent way of constructing signatures on arbitrary messages.
▪ Selective forgery: C forges a signature for a particular message chosen
by C.
▪ Existential forgery: C forges a signature for at least one message. C has
no control over the message. Consequently, this forgery may only be a
minor nuisance to A.

Digital Signature Requirements
1. The signature must be a bit pattern that depends on the message
being signed.
2. The signature must use some information unique to the sender to
prevent both forgery and denial.
3. It must be relatively easy to produce the digital signature.
4. It must be relatively easy to recognize and verify the digital signature.
5. It must be computationally infeasible to forge a digital signature, either
by constructing a new message for an existing digital signature or by
constructing a fraudulent digital signature for a given message.
6. It must be practical to retain a copy of the digital signature in storage.


### Extracted Images
![Lecture_33_19.11_Cryptography_BMK_p1_i0.png](assets/Lecture_33_19.11_Cryptography_BMK_p1_i0.png)

![Lecture_33_19.11_Cryptography_BMK_p6_i0.png](assets/Lecture_33_19.11_Cryptography_BMK_p6_i0.png)

---

## Lecture 35 25.11 Cryptography BMK

### Simple Notes (Key Points)
- Digital Signature Algorithm
- Digital Signature Algorithm
- Key & Secret Number Generation
- Digital Signature Algorithm
- Key Generation

### Detailed Notes
Lecture 35
Digital Signature Algorithm

Digital Signature Algorithm

Key & Secret Number Generation

Signing Process

Digital Signature Algorithm

DSA Signing

DSA Verifying

ElGamal Digital Signatures
Key Generation
Select XA : 1 < XA < q-1
Calculate YA = αXA mod q
Private Key = XA
Public Key  = {q, α, YA}
Signing a Message
Choose random integer K,
1 ≤ K ≤ q-1 and GCD(K, q-1) = 1
Compute S1 = αK mod q
Compute K-1 mod (q-1)
Compute S2 = K-1 (m - XA * S1) mod (q-1)
Signature = (S1, S2)
Verifying a Signature
Compute V1 = αm mod q
Compute V2 = (YA)S1* (S1)S2 mod q
The signature is valid if V1 = V2
How V1 = V2 ?
αm mod q = (YA)S1 * (S1)S2 mod q
αm mod q = (αXA)S1 * (αK)S2 mod q
αm mod q = αXA S1 * αKS2 mod q
αm - XA S1 mod q = αKS2 mod q
m – XA S1 ≡ K S2 mod (q -1)
m – XA S1 ≡ K K-1 (m - XA * S1) mod (q-1)

ElGamal Signature Example
▪ Use field GF(19) q=19 and a=10
▪ Alice computes her key:
• A chooses xA=16 & computes yA=10
16
mod 19 = 4
▪ Alice signs message with hash m=14 as (3,4):
• choosing random K=5 which has gcd(18,5)=1
• computing S1 = 10
5
mod 19 = 3
• finding K-1 mod (q-1) = 5-1 mod 18 = 11
• computing S2 = 11(14-16.3) mod 18 = 4
▪ Any user B can verify the signature by computing
• V1 = 10
14
mod 19 = 16
• V2 = 43.34 = 5184 = 16 mod 19
• since 16 = 16 signature is valid

Schnorr Digital Signatures
▪ Also uses exponentiation in a finite (Galois)
• security based on discrete logarithms
▪ Minimizes message dependent computation
• multiplying a 2n-bit integer with an n-bit integer
▪ Main work can be done in idle time
▪ Have using a prime modulus p
• p–1 has a prime factor q of appropriate size
• typically p 1024-bit and q 160-bit numbers

Schnorr Key Setup
▪ choose suitable primes p , q
▪ choose α  such that  αq = 1 mod q
▪ (α,p,q) are global parameters for all
▪ each user (eg. A) generates a key
• chooses a secret key (number): 0 < sA < q
• compute their public key: vA = α -sA mod q

Schnorr Signature
▪ User signs message by
• choosing random r with 0<r<q and
computing x = αr mod p
• concatenate message with x and hash result
to computing: e = H(M || x)
• computing: y = (r + se) mod q
• signature is pair (e, y)
▪ Any other user can verify the signature as follows:
• computing: x' = αyve mod p
• verifying that: e = H(M || x’)


### Extracted Images
![Lecture_35_25.11_Cryptography_BMK_p2_i0.png](assets/Lecture_35_25.11_Cryptography_BMK_p2_i0.png)

![Lecture_35_25.11_Cryptography_BMK_p3_i0.png](assets/Lecture_35_25.11_Cryptography_BMK_p3_i0.png)

![Lecture_35_25.11_Cryptography_BMK_p4_i0.png](assets/Lecture_35_25.11_Cryptography_BMK_p4_i0.png)

![Lecture_35_25.11_Cryptography_BMK_p4_i1.png](assets/Lecture_35_25.11_Cryptography_BMK_p4_i1.png)

![Lecture_35_25.11_Cryptography_BMK_p4_i2.png](assets/Lecture_35_25.11_Cryptography_BMK_p4_i2.png)

![Lecture_35_25.11_Cryptography_BMK_p5_i0.png](assets/Lecture_35_25.11_Cryptography_BMK_p5_i0.png)

![Lecture_35_25.11_Cryptography_BMK_p5_i1.png](assets/Lecture_35_25.11_Cryptography_BMK_p5_i1.png)

![Lecture_35_25.11_Cryptography_BMK_p5_i2.png](assets/Lecture_35_25.11_Cryptography_BMK_p5_i2.png)

![Lecture_35_25.11_Cryptography_BMK_p5_i3.png](assets/Lecture_35_25.11_Cryptography_BMK_p5_i3.png)

![Lecture_35_25.11_Cryptography_BMK_p6_i0.png](assets/Lecture_35_25.11_Cryptography_BMK_p6_i0.png)

![Lecture_35_25.11_Cryptography_BMK_p7_i0.png](assets/Lecture_35_25.11_Cryptography_BMK_p7_i0.png)

---

## Lecture 37 28.11 Cryptography BMK

### Simple Notes (Key Points)
- Network & System Security
- Network & System Security
- Security Basics
- Security Basics
- ▪ Network Security vs System Security

### Detailed Notes
Lecture 37
Network & System Security

Network & System Security
Security Basics
CIA Triad Diagram
Malicious Software Overview

Security Basics
▪ Network Security vs System Security
• Security Goals: Confidentiality, Integrity, Availability
• Threats and Vulnerabilities
• Attacker Types

CIA Triad Diagram
Confidentiality
Integrity
Availability

Malicious Software Overview
▪ Definition of Malware
• Malware Behavior
• Propagation Techniques

Virus, Worms & Trojans
Computer Viruses
Worms
Virus vs Worm vs Trojan
Trojans

Computer Viruses
▪ Definition & Behavior
• Components: Infection Mechanism, Trigger,Payload
• Types: Boot, File, Macro Virus
• Detection Techniques

Worms
▪ Definition & Propagation
• Self-replicating nature
• Network-level infection
• Examples

Virus vs Worm vs Trojan
Virus
Worm
Trojan

Trojans
▪ Masquerading Behavior
• Backdoors & Keyloggers
• Prevention & Detection

Advanced Malware Types & Defense
Malware Classification
Viruses
Worms
Trojans
Spyware
Ransomware

Other Malware
▪ Spyware
• Adware
• Ransomware
• Rootkits

Defense Techniques
▪ Antivirus & Anti-malware Tools
• Sandboxing
• Patch Management
• User Awareness

IPSec (IP & Network Layer Security)
Overview
▪ Need for IP Layer Security
• Security Associations (SA)
• Key Management

IPSec Protocols
▪ Authentication Header (AH)
• Encapsulating Security Payload (ESP)
• Transport Mode vs Tunnel Mode

IPSec Building Blocks
AH
ESP
SA

Firewall Concepts
▪ Packet Filtering
• Stateful Firewalls
• Next-Generation Firewalls

IDS / IPS
▪ Intrusion Detection System
• Intrusion Prevention System
• Signature-based vs Anomaly-based Detection

Network Security Architecture
Firewall
IDS/IPS
VPN
DMZ

VPN Technologies
▪ Tunneling Concepts
• Site-to-Site VPN
• Remote Access VPN

Web Threats
▪ SQL Injection
• XSS
• Session Hijacking
• Cookie Theft

Web Security Layers
Input Validation
Authentication
Session Security
Output Encoding

Email Security
▪ Phishing & Spoofing
• PGP
• S/MIME
• SPF, DKIM, DMARC

System Security Basics
▪ Authentication Mechanisms
• Access Control Models
• Least Privilege Principle
• Operating System Hardening

System Security Layers
User
OS
Network
Applications

Security Tools
▪ Packet Analyzers (Wireshark)
• Vulnerability Scanners (Nmap, Nessus)
• Antivirus / EDR Tools


### Extracted Images
![Lecture_37_28.11_Cryptography_BMK_p4_i0.png](assets/Lecture_37_28.11_Cryptography_BMK_p4_i0.png)

![Lecture_37_28.11_Cryptography_BMK_p4_i1.png](assets/Lecture_37_28.11_Cryptography_BMK_p4_i1.png)

![Lecture_37_28.11_Cryptography_BMK_p4_i2.png](assets/Lecture_37_28.11_Cryptography_BMK_p4_i2.png)

![Lecture_37_28.11_Cryptography_BMK_p4_i3.png](assets/Lecture_37_28.11_Cryptography_BMK_p4_i3.png)

![Lecture_37_28.11_Cryptography_BMK_p9_i0.png](assets/Lecture_37_28.11_Cryptography_BMK_p9_i0.png)

![Lecture_37_28.11_Cryptography_BMK_p9_i1.png](assets/Lecture_37_28.11_Cryptography_BMK_p9_i1.png)

![Lecture_37_28.11_Cryptography_BMK_p9_i2.png](assets/Lecture_37_28.11_Cryptography_BMK_p9_i2.png)

![Lecture_37_28.11_Cryptography_BMK_p9_i3.png](assets/Lecture_37_28.11_Cryptography_BMK_p9_i3.png)

![Lecture_37_28.11_Cryptography_BMK_p9_i4.png](assets/Lecture_37_28.11_Cryptography_BMK_p9_i4.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i0.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i0.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i1.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i1.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i2.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i2.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i3.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i3.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i4.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i4.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i5.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i5.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i6.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i6.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i7.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i7.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i8.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i8.png)

![Lecture_37_28.11_Cryptography_BMK_p11_i9.png](assets/Lecture_37_28.11_Cryptography_BMK_p11_i9.png)

![Lecture_37_28.11_Cryptography_BMK_p16_i0.png](assets/Lecture_37_28.11_Cryptography_BMK_p16_i0.png)

![Lecture_37_28.11_Cryptography_BMK_p16_i1.png](assets/Lecture_37_28.11_Cryptography_BMK_p16_i1.png)

![Lecture_37_28.11_Cryptography_BMK_p16_i2.png](assets/Lecture_37_28.11_Cryptography_BMK_p16_i2.png)

![Lecture_37_28.11_Cryptography_BMK_p16_i3.png](assets/Lecture_37_28.11_Cryptography_BMK_p16_i3.png)

![Lecture_37_28.11_Cryptography_BMK_p16_i4.png](assets/Lecture_37_28.11_Cryptography_BMK_p16_i4.png)

![Lecture_37_28.11_Cryptography_BMK_p16_i5.png](assets/Lecture_37_28.11_Cryptography_BMK_p16_i5.png)

![Lecture_37_28.11_Cryptography_BMK_p19_i0.png](assets/Lecture_37_28.11_Cryptography_BMK_p19_i0.png)

![Lecture_37_28.11_Cryptography_BMK_p19_i1.png](assets/Lecture_37_28.11_Cryptography_BMK_p19_i1.png)

![Lecture_37_28.11_Cryptography_BMK_p19_i2.png](assets/Lecture_37_28.11_Cryptography_BMK_p19_i2.png)

![Lecture_37_28.11_Cryptography_BMK_p19_i3.png](assets/Lecture_37_28.11_Cryptography_BMK_p19_i3.png)

![Lecture_37_28.11_Cryptography_BMK_p19_i4.png](assets/Lecture_37_28.11_Cryptography_BMK_p19_i4.png)

![Lecture_37_28.11_Cryptography_BMK_p19_i5.png](assets/Lecture_37_28.11_Cryptography_BMK_p19_i5.png)

![Lecture_37_28.11_Cryptography_BMK_p19_i6.png](assets/Lecture_37_28.11_Cryptography_BMK_p19_i6.png)

![Lecture_37_28.11_Cryptography_BMK_p19_i7.png](assets/Lecture_37_28.11_Cryptography_BMK_p19_i7.png)

![Lecture_37_28.11_Cryptography_BMK_p22_i0.png](assets/Lecture_37_28.11_Cryptography_BMK_p22_i0.png)

![Lecture_37_28.11_Cryptography_BMK_p22_i1.png](assets/Lecture_37_28.11_Cryptography_BMK_p22_i1.png)

![Lecture_37_28.11_Cryptography_BMK_p22_i2.png](assets/Lecture_37_28.11_Cryptography_BMK_p22_i2.png)

![Lecture_37_28.11_Cryptography_BMK_p22_i3.png](assets/Lecture_37_28.11_Cryptography_BMK_p22_i3.png)

![Lecture_37_28.11_Cryptography_BMK_p22_i4.png](assets/Lecture_37_28.11_Cryptography_BMK_p22_i4.png)

![Lecture_37_28.11_Cryptography_BMK_p25_i0.png](assets/Lecture_37_28.11_Cryptography_BMK_p25_i0.png)

![Lecture_37_28.11_Cryptography_BMK_p25_i1.png](assets/Lecture_37_28.11_Cryptography_BMK_p25_i1.png)

![Lecture_37_28.11_Cryptography_BMK_p25_i2.png](assets/Lecture_37_28.11_Cryptography_BMK_p25_i2.png)

![Lecture_37_28.11_Cryptography_BMK_p25_i3.png](assets/Lecture_37_28.11_Cryptography_BMK_p25_i3.png)

![Lecture_37_28.11_Cryptography_BMK_p25_i4.png](assets/Lecture_37_28.11_Cryptography_BMK_p25_i4.png)

![Lecture_37_28.11_Cryptography_BMK_p25_i5.png](assets/Lecture_37_28.11_Cryptography_BMK_p25_i5.png)

![Lecture_37_28.11_Cryptography_BMK_p25_i6.png](assets/Lecture_37_28.11_Cryptography_BMK_p25_i6.png)

---

## Lecture 3 25.7 Cryptography BMK

### Simple Notes (Key Points)
- Security Services
- Security Services (X.800)
- ▪ X.800 standard defines a security service as a service that is
- that ensures security of the systems or of data transfers.
- Security Services

### Detailed Notes
Lecture 3
Security Services

Security Services (X.800)
▪ X.800 standard defines a security service as a service that is
provided by a protocol layer of communicating open systems and
that ensures security of the systems or of data transfers.

Security Services
Authentication
Peer Entity
Authentication
Data Origin
Authentication
Access Control Data
Confidentiality
Connection
Confidentiality
Connection less
Confidentiality
Selective Repeat
Confidentiality
Traffic Flow
Confidentiality
Data Integrity
Connection
Integrity with
recovery
Connection
Integrity with
out recovery
Selective Field
Connection
Integrity
Connection less
Integrity
Selective Field
Connection less
Integrity
Non Repudiation
Non Repudiation
Origin
Non Repudiation
Destination

Authentication
▪ Authentication is the assurance that the communicating entity is
the one that it claims to be.
Who you are ?
(biometrics)
Physical
authentication
where you are ?
What you know ?
Password
One-time Passwords
Network address
1. Peer Entity Authentication:
Used in association with a
logical connection to provide
confidence in the identity of
the entities connected.
2. Data-Origin Authentication: In
a connectionless transfer,
provides assurance that the
source of received data is as
claimed.

Access Control
▪ Access control is the prevention of unauthorized use of a resource
▪ This service controls who can have access to a resource, under
what conditions access can occur, and what those accessing the
resource are allowed to do).

Data Confidentiality
▪ Data confidentiality is the protection of data from unauthorized
disclosure.
1. Connection Confidentiality: The
protection of all user data on a
connection.
2. Connectionless Confidentiality: The
protection of all user data in a single
data block.
3. Selective-Field Confidentiality: The
confidentiality of selected fields
within the user data on a connection
or in a single data block.
4. Traffic-Flow Confidentiality: The
protection of the information that
might be derived from observation of
traffic flows.

Data Integrity
▪ Data integrity is the assurance that data received are exactly as
sent by an authorized entity (i.e., contain no modification,
insertion, deletion, or replay).

Data Integrity (Cont…)
▪ Connection Integrity with Recovery: Provides integrity of all user
data on a connection and detects any modification, insertion,
deletion, or replay of any data with recovery attempted.
▪ Connection Integrity without Recovery: As above, but provides
only detection without recovery.
▪ Selective-Field Connection Integrity: Provides integrity of selected
fields within the user data and takes the form of determination of
whether the selected fields have been modified, inserted, deleted,
or replayed.

Data Integrity (Cont…)
▪ Connectionless Integrity: Provides integrity of a single
connectionless data block and may take the form of detection of
data modification. Additionally, a limited form of replay detection
may be provided.
▪ Selective-Field Connectionless Integrity: Provides integrity of
selected fields within a single connectionless data block; takes the
form of determination of whether the selected fields have been
modified.

Non Repudiation
▪ Nonrepudiation is the assurance that someone cannot deny
something.
▪ Typically, nonrepudiation refers to the ability to ensure that a
communication cannot deny the authenticity of their signature on
a document or the sending of a message that they originated.
Bank
Transfer Rs. 1,00,000
To Bank
I have never
requested to transfer
Rs. 1,00,000
to Bank
User A
After few days

Non Repudiation (Cont…)
▪ Nonrepudiation-Origin: Proof that the message was sent by the
specified party.
▪ Nonrepudiation-Destination: Proof that the message was
received by the specified party.


### Extracted Images
![Lecture_3_25.7_Cryptography_BMK_p4_i0.jpg](assets/Lecture_3_25.7_Cryptography_BMK_p4_i0.jpg)

![Lecture_3_25.7_Cryptography_BMK_p4_i1.png](assets/Lecture_3_25.7_Cryptography_BMK_p4_i1.png)

![Lecture_3_25.7_Cryptography_BMK_p5_i0.jpg](assets/Lecture_3_25.7_Cryptography_BMK_p5_i0.jpg)

![Lecture_3_25.7_Cryptography_BMK_p6_i0.jpg](assets/Lecture_3_25.7_Cryptography_BMK_p6_i0.jpg)

![Lecture_3_25.7_Cryptography_BMK_p7_i0.jpg](assets/Lecture_3_25.7_Cryptography_BMK_p7_i0.jpg)

![Lecture_3_25.7_Cryptography_BMK_p10_i0.png](assets/Lecture_3_25.7_Cryptography_BMK_p10_i0.png)

![Lecture_3_25.7_Cryptography_BMK_p10_i1.jpg](assets/Lecture_3_25.7_Cryptography_BMK_p10_i1.jpg)

---

## Lecture 4 29.7 Cryptography BMK

### Simple Notes (Key Points)
- Security Mechanisms
- Security Mechanisms (X.800)
- ▪ Specific security mechanisms: Integrated into the appropriate
- protocol layer in order to provide some of the OSI security
- ▪ Pervasive security mechanisms: Not integrated to any particular

### Detailed Notes
Lecture 4
Security Mechanisms

Security Mechanisms (X.800)
▪ Specific security mechanisms: Integrated into the appropriate
protocol layer in order to provide some of the OSI security
services.
▪ Pervasive security mechanisms: Not integrated to any particular
OSI security service or protocol layer

Security Mechanism (Specific Security)
▪ Encipherment: Hiding or covering data using mathematical
algorithms.
▪ Digital Signature: The sender can electronically sign the data and
the receiver can electronically verify the signature.
▪ Access Control: A variety of mechanisms that enforce access
rights to resources.
▪ Data Integrity: A variety of mechanisms used to assure the
integrity of a data unit or stream of data units.
▪ Authentication Exchange: Two entities exchange some messages
to prove their identity to each other.

Security Mechanism (Specific security)
▪ Traffic Padding: The insertion of bits into gaps in a data stream to
frustrate traffic analysis attempts.
▪ Routing Control: Selecting and continuously changing routes
between sender and receiver to prevent opponent from
eavesdropping.
▪ Notarization: The use of a trusted third party to assure and
control the communication.

Security Mechanism (Pervasive security)
▪ Trusted Functionality
▪ Security Label
▪ Event Detection
▪ Security Audit Trail
▪ Security Recovery


---

## Lecture 5 30.7 Cryptography BMK

### Simple Notes (Key Points)
- Classical Ciphers
- Symmetric cipher models
- ▪ Symmetric cipher models
- ▪ Substitution ciphers
- ▪ Transposition ciphers

### Detailed Notes
UNIT-3
Classical Ciphers

Lecture 5
Symmetric cipher models

Outline
▪ Symmetric cipher models
▪ Substitution ciphers
▪ Transposition ciphers
▪ Steganography

Encryption and Decryption
Sender ReceiverEncryption Decryption
f7#erHello Hello

Symmetric Cipher Model (Conventional Encryption)
Plaintext
input
Plaintext
output
Encryption Algorithm
(e.g. AES)
Decryption Algorithm
(reverse of encryption
algorithm)
Secret key shared by
sender and recipient
X
Secret key shared by
sender and recipient
K
Transmitted
cipher text
Y = E(K, X)
▪ An original message is known as the plaintext, while the coded
message is called the ciphertext.
▪ The process of converting from plaintext to ciphertext is known as
enciphering or encryption; restoring the plaintext from the
ciphertext is deciphering or decryption.
▪ Plaintext is the original intelligible message or data that is fed into
the algorithm as input.
▪ Encryption algorithm performs various substitutions and
transformations on the plaintext.
▪ The secret key is also input to the encryption algorithm.
▪ The key is a value independent of the plaintext and of the
algorithm.
▪ The algorithm will produce a different output depending on the
specific key being used at the time.
K
X
▪ Ciphertext is the scrambled message produced as output.
▪ It depends on the plaintext and the secret key.
▪ The ciphertext is an apparently random stream of data and, as it
stands, is unintelligible.
▪ Decryption algorithm is essentially the encryption algorithm run in
reverse.
▪ It takes the ciphertext and the secret key and produces the original
plaintext.



Cryptanalysis and Brute-Force Attack
▪ Cryptanalysis: Cryptanalytic attacks rely on the nature of the
algorithm and some knowledge of the general characteristics of
the plaintext or even some sample plaintext–ciphertext pairs.
▪ This type of attack exploits the characteristics of the algorithm to
attempt to derive a specific plaintext or to derive the key being
used.
▪ Brute-force attack: The attacker tries every possible key on a
piece of ciphertext until an intelligible translation into plaintext is
obtained.
▪ On average, half of all possible keys must be tried to achieve
success.

Attacks on Encrypted Messages
Type of Attack Known to cryptanalyst
Ciphertext Only Encryption algorithm, Ciphertext

Attacks on Encrypted Messages
Type of Attack Known to cryptanalyst
Known Plaintext Encryption algorithm, Ciphertext, One or more plaintext-
cipher text pairs formed with the secret key

Attacks on Encrypted Messages
Type of Attack Known to cryptanalyst
Chosen Plaintext Encryption algorithm, Ciphertext, Plaintext message chosen by
cryptanalyst

Attacks on Encrypted Messages
Type of Attack Known to cryptanalyst
Chosen
Ciphertext
Encryption algorithm, Ciphertext, Ciphertext chosen by
cryptanalyst, with its corresponding decrypted plaintext
generated with the secret key

Attacks on Encrypted Messages
Type of Attack Known to cryptanalyst
Chosen text Encryption algorithm, Ciphertext, Plaintext chosen by
cryptanalyst, with its corresponding ciphertext generated with
the secret key , Ciphertext chosen by cryptanalyst, with its
corresponding decrypted plaintext generated with the secret
key


### Extracted Images
![Lecture_5_30.7_Cryptography_BMK_p1_i0.png](assets/Lecture_5_30.7_Cryptography_BMK_p1_i0.png)

![Lecture_5_30.7_Cryptography_BMK_p5_i0.png](assets/Lecture_5_30.7_Cryptography_BMK_p5_i0.png)

![Lecture_5_30.7_Cryptography_BMK_p5_i1.png](assets/Lecture_5_30.7_Cryptography_BMK_p5_i1.png)

![Lecture_5_30.7_Cryptography_BMK_p5_i2.png](assets/Lecture_5_30.7_Cryptography_BMK_p5_i2.png)

![Lecture_5_30.7_Cryptography_BMK_p6_i0.png](assets/Lecture_5_30.7_Cryptography_BMK_p6_i0.png)

![Lecture_5_30.7_Cryptography_BMK_p6_i1.png](assets/Lecture_5_30.7_Cryptography_BMK_p6_i1.png)

![Lecture_5_30.7_Cryptography_BMK_p8_i0.png](assets/Lecture_5_30.7_Cryptography_BMK_p8_i0.png)

![Lecture_5_30.7_Cryptography_BMK_p9_i0.png](assets/Lecture_5_30.7_Cryptography_BMK_p9_i0.png)

![Lecture_5_30.7_Cryptography_BMK_p10_i0.png](assets/Lecture_5_30.7_Cryptography_BMK_p10_i0.png)

![Lecture_5_30.7_Cryptography_BMK_p11_i0.png](assets/Lecture_5_30.7_Cryptography_BMK_p11_i0.png)

---

## Lecture 6 1.8 Cryptography BMK

### Simple Notes (Key Points)
- 1) Caesar Cipher
- 2) Monoalphabetic Cipher
- 3) Playfair Cipher
- 4) Hill Cipher
- 5) Polyalphabetic Ciphers

### Detailed Notes
Lecture 6
Caesar & Monoalphabetic

Substitution Techniques
▪ A substitution technique is one in which the letters of plaintext
are replaced by other letters or by numbers or symbols.
1) Caesar Cipher
2) Monoalphabetic Cipher
3) Playfair Cipher
4) Hill Cipher
5) Polyalphabetic Ciphers
6) One-Time Pad

1) Caesar Cipher
▪ The Caesar cipher involves replacing each letter of the alphabet
with the letter standing three places further down the alphabet.
▪ In encryption each plaintext letter P, substitute the ciphertext
letter C:
▪ For decryption algorithm is:
C = E(k, P) = (P + k) mod 26
C = E(3, P) = (P + 3) mod 26
P = D(k, C) = (C - k) mod 26

Caesar Cipher (Cont…)
a b c d e f g h i j k l m
0 1 2 3 4 5 6 7 8 9 10 11 12
n o p q r s t u v w x y z
13 14 15 16 17 18 19 20 21 22 23 24 25
C = E(3, P) = (P + 3) mod 26
plain:  a b c d e f g h i j k l m n o p q r s t u v w x y z
cipher: d e f g h i j k l m n o p q r s t u v w x y z a b c
Example:
Plaintext:      THE QUICK BROWN FOX
Ciphertext:   WKH TXLFN EURZQ IRA
▪ Let us assign a numerical equivalent to each letter

Brute force attack on Caesar Cipher
▪ The encryption and decryption algorithms are known.
▪ There are only 25 keys to try.
▪ The language of the plaintext is known and easily recognizable.

Brute force attack on Caesar Cipher
Key Transformed text
1 YMJ VZNHP GWTBS KTC
2 XLI UYMGO FVSAR JSB
3 WKH TXLFN EURZQ IRA
4 VJG SWKEM DTQYP HQZ
5 UIF RVJDL CSPXOGPY
6 THE QUICK BROWN FOX
7 SGD PTHBJ AQNVM ENW
8 RFC OSGAI ZPMUL DMV
9 QEB NRFZH YOLTK CLU
10 PDA MQEYG XNKSJ BKT
11 OCZ LPDXF WMJRI AJS
12 NBY KOCWE VLIQH ZIR
13 MAX JNBVD UKHPG YHQ
Key Transformed text
14 LZW IMAUC TJGOF XGP
15 KYV HLZTB SIFNE WFO
16 JXU GKYSA RHEMD VEN
17 IWT FJXRZ QGDLC UDM
18 HVS EIWQY PFCKB TCL
19 GUR DHVPX OEBJA SBK
20 FTQ CGUOW NDAIZ RAJ
21 ESP BFTNV MCZHY QZI
22 DRO AESMU LBYGX PYH
23 CQN ZDRLT KAXFW OXG
24 BPM YCQKS JZWEV NWF
25 AOL XBPJR IYVDU MVE
Ciphertext: ZNK WAOIQ HXUCT LUD

Substitution Techniques
1) Caesar Cipher
2) Monoalphabetic Cipher
3) Playfair Cipher
4) Hill Cipher
5) Polyalphabetic Ciphers
6) One-Time Pad

2) Monoalphabetic Cipher (Simple substitution)
▪ It is an improvement to the Caesar Cipher.
▪ Instead of shifting the alphabets by some number, this scheme
uses some permutation of the letters in alphabet.
▪ The sender and the receiver decide on a randomly selected
permutation of the letters of the alphabet.
▪ With 26 letters in alphabet, the possible permutations are 26!
which is equal to 4x1026.
plain:  a b c d e f g h i j k l m n o p q r s t u v w x y z
cipher: y n l k x b s h m i w d p j r o q v f e a u g t z c

Relative Frequency of Letters in English Text

Attack on Monoalphabetic Cipher
▪ The relative frequencies of the letters in the ciphertext (in
percentages) are
Ciphertext:
uzqsovuohxmopvgpozpevsgzwszopfpesxudbmetsxaizvuephzhmdzshzowsf
pappdtsvpquzwymxuzuhsxepyepopdzszufpombzwpfupzhmdjudtmohmq
▪ In our ciphertext, the most common digram is ZW, which appears
three times. So equate  Z with t, W with h and P with e.
▪ Now notice that the sequence ZWP appears in the ciphertext, and
we can translate that sequence as “the.”

Actual Message
it was disclosed yesterday that several informal but
direct contacts have been made with political
representatives of the viet cong in moscow

Attack on Monoalphabetic Cipher (Cont…)
▪ If the cryptanalyst knows the nature of the plaintext, then the
analyst can exploit the regularities of the language.
▪ The relative frequency of the letters can be determined and
compared to a standard frequency distribution for English.
▪ If the message were long enough, this technique alone might be
sufficient, but because this is a relatively short message, we
cannot expect an exact match.


### Extracted Images
![Lecture_6_1.8_Cryptography_BMK_p9_i0.png](assets/Lecture_6_1.8_Cryptography_BMK_p9_i0.png)

![Lecture_6_1.8_Cryptography_BMK_p10_i0.png](assets/Lecture_6_1.8_Cryptography_BMK_p10_i0.png)

---

## Lecture 7 5.8 Cryptography BMK

### Simple Notes (Key Points)
- Playfair Cipher
- 1) Caesar Cipher
- 2) Monoalphabetic Cipher
- 3) Playfair Cipher
- 4) Hill Cipher

### Detailed Notes
Lecture 7
Playfair Cipher

Substitution Techniques
1) Caesar Cipher
2) Monoalphabetic Cipher
3) Playfair Cipher
4) Hill Cipher
5) Polyalphabetic Ciphers
6) One-Time Pad

3) Playfair Cipher
▪ The Playfair algorithm is based on a 5 × 5 matrix (key) of letters.
▪ The matrix is constructed by filling in the letters of the keyword
(minus duplicates) from left to right and from top to bottom, and
then filling in the remainder of the matrix with the remaining
letters in alphabetic order. The letters I and J count as one letter.
Example:
Keyword= OCCURRENCE
Plaintext= TALL TREES
O C U R E
N A B D F
G H I/J K L
M P Q S T
V W X Y Z

Playfair Cipher - Encrypt Plaintext
▪ Playfair, treats digrams (two letters) in the plaintext as single units
and translates these units into ciphertext digrams.
▪ Make Pairs of letters add filler letter “X” if same letter appears in
a pair.
▪ If there is an odd number of letters, then add uncommon letter to
complete digram, a X/Z may be added to the last letter.
Plaintext= TALL TREES
Plaintext= TA LX LT RE ES

Playfair Cipher - Encrypt Plaintext
▪ Map each pair in key matrix
O C U R E
N A B D F
G H I/J K L
M P Q S T
V W X Y Z
▪ If the letters appear on the same row, replace them with the
letters to their immediate right respectively, wrapping around to
the left side of the row if necessary.
▪ For example, using the table above, the letter pair RE would be
encoded as EO.
Plaintext= TA LX LT RE ES
▪ If the letters appear on the same column, replace them with the
letters immediately below, wrapping around to the top if
necessary.
▪ For example, using the table above, the letter pair LT would be
encoded as TZ.
▪ If the letters are on different rows and columns, replace them
with the letters on other corner of the same row.
▪ The order is important - the first letter of the pair should be
replaced first.
▪ For example, using the table above, the letter pair TA would be
encoded as PF.
Ciphertext= PF IZ TZ EO RT

Playfair Cipher Examples
1. Key= “engineering ” Plaintext=”test this process ”
2. Key= “keyword ” Plaintext=”come to the window ”
3. Key= “moonmission ” Plaintext=”greet ”
E N G I R
A B C D F
H K L M O
P Q S T U
V W X Y Z
Encrypted Message:
pi tu pm gt ue lf gp xg
K E Y W O
R D A B C
F G H I L
M N P Q S
T U V X Z
Encrypted Message:
lc nk zk vf yo gq ce
bw
M O N I S
A B C D E
F G H K L
P Q R T U
V W X Y Z
Encrypted Message:
hq cz du


---

## Lecture 8 8.8 Cryptography BMK

### Simple Notes (Key Points)
- Hill Cipher
- 1) Caesar Cipher
- 2) Monoalphabetic Cipher
- 3) Playfair Cipher
- 4) Hill Cipher

### Detailed Notes
Lecture 8
Hill Cipher

Substitution Techniques
1) Caesar Cipher
2) Monoalphabetic Cipher
3) Playfair Cipher
4) Hill Cipher
5) Polyalphabetic Ciphers
6) One-Time Pad

4) Hill Cipher
▪ Hill cipher is based on linear algebra
▪ Each letter is represented by numbers from 0 to 25 and
calculations are done modulo 26.
▪ Encryption and decryption can be given by the following formula:
Encryption:
Decryption:
C=PK mod 26
P=CK-1 mod 26

Hill Cipher Encryption
▪ To encrypt a message using the Hill Cipher we must first turn our
keyword and plaintext into a matrix (a 2 x 2 matrix or a 3 x 3
matrix, etc).
Example: Key = “HILL”, Plaintext =
“EXAM”a b c d e f g h i j k l m
0 1 2 3 4 5 6 7 8 9 10 11 12
n o p q r s t u v w x y z
13 14 15 16 17 18 19 20 21 22 23 24 25

Hill Cipher Encryption (Cont…)
C=PK mod 26
Ciphertext = “ELSC”

THE HILLALGORITHM This encryption algorithm takes m successive plaintext letters
and substitutes for them ciphertext letters.
For , m=3 the system can be described as



pay : (15 0 24)

mor : (12 14 17)

emo : (4 12 14)

ney : (13 4 24)



Hill Cipher Decryption
Step:1 Find Inverse of key matrix
Step:2 Multiply the Multiplicative Inverse of the Determinant by the
Adjoin Matrix
Step:3 Multiply inverse key matrix with ciphertext matrix to obtain
plaintext matrix
P=CK-1 mod 26

Step: 1 Inverse of key matrix
2 X 2 inverse of matrix
3 X 3 inverse of matrix

Step: 1 Inverse of key matrix
▪ -11 mod 26 = 15
▪ Because, modulo for negative
number is = N- (B%N)
= 26 – (11%26)

Step: 2 Modular (Multiplicative) inverse
▪ The inverse of a number A is 1/A since A * 1/A = 1
e.g. the inverse of 5 is 1/5
▪ In modular arithmetic we do not have a division operation.
▪ The modular inverse of A (mod C) is A-1
▪ (A * A-1) ≡ 1 (mod C)
Example:
▪ The modular inverse of A mod C is the A-1 value that makes
A * A-1 mod C = 1
A = 3, C = 11
Since (3*4) mod 11 = 1, 4 is modulo inverse of 3
A = 10, C = 17 , A-1 = ?
12

Step 2: Modular (Multiplicative) inverse
Determinants’ multiplicative inverse Modulo 26
Determinant 1 3 5 7 9 11 15 17 19 21 23 25
Inverse Modulo 26 1 9 21 15 3 19 7 23 11 5 17 25

Step 2: Multiply with adjoin of matrix


### Extracted Images
![Lecture_8_8.8_Cryptography_BMK_p3_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p3_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p4_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p4_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p4_i1.png](assets/Lecture_8_8.8_Cryptography_BMK_p4_i1.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i1.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i1.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i2.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i2.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i3.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i3.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i4.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i4.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i5.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i5.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i6.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i6.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i7.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i7.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i8.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i8.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i9.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i9.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i10.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i10.png)

![Lecture_8_8.8_Cryptography_BMK_p5_i11.png](assets/Lecture_8_8.8_Cryptography_BMK_p5_i11.png)

![Lecture_8_8.8_Cryptography_BMK_p6_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p6_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p6_i1.png](assets/Lecture_8_8.8_Cryptography_BMK_p6_i1.png)

![Lecture_8_8.8_Cryptography_BMK_p6_i2.png](assets/Lecture_8_8.8_Cryptography_BMK_p6_i2.png)

![Lecture_8_8.8_Cryptography_BMK_p7_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p7_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p7_i1.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p7_i1.jpg)

![Lecture_8_8.8_Cryptography_BMK_p7_i2.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p7_i2.jpg)

![Lecture_8_8.8_Cryptography_BMK_p8_i0.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p8_i0.jpg)

![Lecture_8_8.8_Cryptography_BMK_p9_i0.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p9_i0.jpg)

![Lecture_8_8.8_Cryptography_BMK_p10_i0.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p10_i0.jpg)

![Lecture_8_8.8_Cryptography_BMK_p11_i0.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p11_i0.jpg)

![Lecture_8_8.8_Cryptography_BMK_p12_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p12_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p12_i1.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p12_i1.jpg)

![Lecture_8_8.8_Cryptography_BMK_p12_i2.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p12_i2.jpg)

![Lecture_8_8.8_Cryptography_BMK_p12_i3.jpg](assets/Lecture_8_8.8_Cryptography_BMK_p12_i3.jpg)

![Lecture_8_8.8_Cryptography_BMK_p14_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p14_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p14_i1.png](assets/Lecture_8_8.8_Cryptography_BMK_p14_i1.png)

![Lecture_8_8.8_Cryptography_BMK_p15_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p15_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p15_i1.png](assets/Lecture_8_8.8_Cryptography_BMK_p15_i1.png)

![Lecture_8_8.8_Cryptography_BMK_p15_i2.png](assets/Lecture_8_8.8_Cryptography_BMK_p15_i2.png)

![Lecture_8_8.8_Cryptography_BMK_p17_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p17_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p17_i1.png](assets/Lecture_8_8.8_Cryptography_BMK_p17_i1.png)

![Lecture_8_8.8_Cryptography_BMK_p18_i0.png](assets/Lecture_8_8.8_Cryptography_BMK_p18_i0.png)

![Lecture_8_8.8_Cryptography_BMK_p18_i1.png](assets/Lecture_8_8.8_Cryptography_BMK_p18_i1.png)

---

## Lecture 9 12.8 Cryptography BMK

### Simple Notes (Key Points)
- 1) Caesar Cipher
- 2) Monoalphabetic Cipher
- 3) Playfair Cipher
- 4) Hill Cipher
- 5) Polyalphabetic Ciphers

### Detailed Notes
Lecture 9
Polyalphabetic & One time pad

Substitution Techniques
1) Caesar Cipher
2) Monoalphabetic Cipher
3) Playfair Cipher
4) Hill Cipher
5) Polyalphabetic Ciphers
6) One-Time Pad

5) Polyalphabetic Cipher
▪ Monoalphabetic cipher encoded using only one fixed alphabet
▪ Polyalphabetic cipher is a substitution cipher in which the cipher
alphabet for the plain alphabet may be different at different
places during the encryption process.
1. Vigenere cipher
2. Vernam cipher

Vigenere Cipher
Keyword : DECEPTIVE
Key : DECEPTIVEDECEPTIVEDECEPTIVE
Plaintext : WEAREDISCOVEREDSAVEYOURSELF

Vigenere Cipher

Vigenere Cipher

Vigenere Cipher

Vigenere Cipher

Vigenere Cipher
Keyword : DECEPTIVE
Key : DECEPTIVEDECEPTIVEDECEPTIVE
Plaintext : WEAREDISCOVEREDSAVEYOURSELF
Ciphertext : ZICVTWQNGRZGVTWAVZHCQYGLMGJ
An analyst looking at only the ciphertext would detect the repeated
sequences VTW at a displacement of 9 and make the assumption that the
keyword is either three or nine letters in length.
Keyword    : DECEPTIVE
Key             : DECEPTIVEWEAREDISCOVEREDSAV
Plaintext    : WEAREDISCOVEREDSAVEYOURSELF
This system
is referred as
an autokey
system

Vigenere Cipher Autokey System

Vernam Cipher
▪ The ciphertext is generated by applying the logical XOR operation
to the individual bits of plaintext and the key stream.

Vernam Cipher

Substitution Techniques
1) Caesar Cipher
2) Monoalphabetic Cipher
3) Playfair Cipher
4) Hill Cipher
5) Polyalphabetic Ciphers
6) One-Time Pad

One time pad
▪ The one-time pad, which is a provably secure cryptosystem,
was developed by Gilbert Vernam in 1918.
▪ The message is represented as a binary string (a sequence of 0’s
and 1’susing a coding mechanism such as ASCII coding.
▪ The key is a truly random sequence of 0’s and 1’s of the same
length as the message.
▪ message =‘IF’
▪ then its ASCII code =(1001001 1000110)
▪ key = (1010110 0110001)
▪ Encryption:
• 1001001 1000110 plaintext
• 1010110 0110001 key
• 0011111 1110110 ciphertext




### Extracted Images
![Lecture_9_12.8_Cryptography_BMK_p4_i0.png](assets/Lecture_9_12.8_Cryptography_BMK_p4_i0.png)

![Lecture_9_12.8_Cryptography_BMK_p4_i1.png](assets/Lecture_9_12.8_Cryptography_BMK_p4_i1.png)

![Lecture_9_12.8_Cryptography_BMK_p5_i0.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p5_i0.jpg)

![Lecture_9_12.8_Cryptography_BMK_p5_i1.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p5_i1.jpg)

![Lecture_9_12.8_Cryptography_BMK_p5_i2.png](assets/Lecture_9_12.8_Cryptography_BMK_p5_i2.png)

![Lecture_9_12.8_Cryptography_BMK_p6_i0.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p6_i0.jpg)

![Lecture_9_12.8_Cryptography_BMK_p6_i1.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p6_i1.jpg)

![Lecture_9_12.8_Cryptography_BMK_p6_i2.png](assets/Lecture_9_12.8_Cryptography_BMK_p6_i2.png)

![Lecture_9_12.8_Cryptography_BMK_p7_i0.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p7_i0.jpg)

![Lecture_9_12.8_Cryptography_BMK_p7_i1.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p7_i1.jpg)

![Lecture_9_12.8_Cryptography_BMK_p7_i2.png](assets/Lecture_9_12.8_Cryptography_BMK_p7_i2.png)

![Lecture_9_12.8_Cryptography_BMK_p8_i0.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p8_i0.jpg)

![Lecture_9_12.8_Cryptography_BMK_p8_i1.png](assets/Lecture_9_12.8_Cryptography_BMK_p8_i1.png)

![Lecture_9_12.8_Cryptography_BMK_p8_i2.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p8_i2.jpg)

![Lecture_9_12.8_Cryptography_BMK_p8_i3.png](assets/Lecture_9_12.8_Cryptography_BMK_p8_i3.png)

![Lecture_9_12.8_Cryptography_BMK_p9_i0.png](assets/Lecture_9_12.8_Cryptography_BMK_p9_i0.png)

![Lecture_9_12.8_Cryptography_BMK_p9_i1.png](assets/Lecture_9_12.8_Cryptography_BMK_p9_i1.png)

![Lecture_9_12.8_Cryptography_BMK_p10_i0.png](assets/Lecture_9_12.8_Cryptography_BMK_p10_i0.png)

![Lecture_9_12.8_Cryptography_BMK_p10_i1.png](assets/Lecture_9_12.8_Cryptography_BMK_p10_i1.png)

![Lecture_9_12.8_Cryptography_BMK_p10_i2.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p10_i2.jpg)

![Lecture_9_12.8_Cryptography_BMK_p10_i3.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p10_i3.jpg)

![Lecture_9_12.8_Cryptography_BMK_p11_i0.jpg](assets/Lecture_9_12.8_Cryptography_BMK_p11_i0.jpg)

![Lecture_9_12.8_Cryptography_BMK_p12_i0.png](assets/Lecture_9_12.8_Cryptography_BMK_p12_i0.png)

![Lecture_9_12.8_Cryptography_BMK_p12_i1.png](assets/Lecture_9_12.8_Cryptography_BMK_p12_i1.png)

![Lecture_9_12.8_Cryptography_BMK_p15_i0.png](assets/Lecture_9_12.8_Cryptography_BMK_p15_i0.png)

---

