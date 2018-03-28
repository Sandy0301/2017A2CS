1.a
AND is used as a logic gate, where 1 and 1 give an output of 1, and 0 and 0 give an output of 1 as well.
b. AND MASK
MASK: #B00001111
C
| label              |opcode                          |operand                         |
|----------------|-------------------------------|-----------------------------|
||IN||
||AND|MASK
||LSL| #4 |
||STO|  RESULT|
||IN|
|| AND|mask|
||OR|RESULT|
||STO|RESULT
||END |
|MASK:|&OF|
|RESULT |&00 |

2.
| label              |opcode                          |operand                         |
|----------------|-------------------------------|-----------------------------|
||LDR|#0|
|LOOP|IN|
||STI|STRING |
||INC|IX|
||CMP|#33
||JNP|LOOP|
||END||
|STRING: