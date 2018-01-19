grammar Contract;

// Lexer Rules
LOWERCASE : ['a'-'z'];
DOUBLE : 'Double' ;
INT : 'Int' ;
DATE : 'Date';
CONTRACT : 'Contract' ;
NUMBERS : [0-9];
OPERANDS : '+' | '-' | '*' | '/' ;
FUNCTIONS : 'and' | 'or' | 'then' | 'scaleX' | 'scale' | 'truncate'; 
TO : '->';
ASSIGNMENT : '::';
LPAREN : '(' ;
RPAREN : ')' ;
ONE : 'one' ;
COMMA : ',' ;
EQUAL : '=' ;
TIMEFUNCT : 'TimeFunct' ;
MKDATE : 'mkDate' ;
GIVE : 'give' ;
WS : [ '\t' | ' ' | '\r' | '\n'| '\u000C' ]+ -> skip ;


// Parser Rules
program : Prog;
Prog : [ Assign | Funccall | Def ]+ ;
TYPES : INT | DOUBLE  | DATE | CONTRACT ;
Name : LOWERCASE + ['a'-'z'_0-9]* ;
Type : TYPES;
Deffunc : LPAREN Type [COMMA Type]*  RPAREN TO Type ;
Defvar : Type ;
Def : Name ASSIGNMENT [Defvar | Deffunc]
	| TIMEFUNCT LPAREN Deffunc RPAREN ;
Assign : Name EQUAL  Expr ;
Int : Name 
	| NUMBERS+ ;
Double : Name 
	   | NUMBERS+ '.' NUMBERS* ;
Date : Name ;
Expr : Expression [Felan]? ;
Felan : Expr OPERANDS Expr [Felan]?;
Expression : Int | Double | Date 
		   | LPAREN Expr RPAREN
		   | Funccall ;
Args : Arg [ COMMA Arg]* ;
Arg : Expr ;
Funccall : Name LPAREN Args RPAREN
		 | MKDATE LPAREN Arg COMMA Arg RPAREN
		 | FUNCTIONS LPAREN Arg COMMA Arg RPAREN
		 | ONE LPAREN RPAREN
		 | GIVE LPAREN Arg RPAREN ;