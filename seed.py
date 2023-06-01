from datetime import date

pwd_hash = 'pbkdf2:sha256:600000$dXZbEh4Xocn4T0tt$1cf903347feae89585d6b5ef2ac50e791ad2e079427a26e167d84e57e1c478b0'
profs = [{'nome':'Professor ADM 1','email':'adm1@prof.com','matricula':'111111111','password':pwd_hash},
         {'nome':'Professor ADM 2','email':'adm2@prof.com','matricula':'222222222','password':pwd_hash},
         {'nome':'Professor ADM 3','email':'adm3@prof.com','matricula':'333333333','password':pwd_hash}
         ]

aulas = [{'nome_disciplina':'Sistemas de Informação','cod_disciplina':'CIC001', 'turma':'A','data_aula':date(2023,5,1),'professor':'111111111', 'alunos_presentes':[['Aluno0', '00000'],
 ['Aluno1', '11111'],
 ['Aluno2', '22222'],
 ['Aluno3', '33333'],
 ['Aluno4', '44444'],
 ['Aluno5', '55555'],
 ['Aluno6', '66666'],
 ['Aluno7', '77777'],
 ['Aluno8', '88888'],
 ['Aluno9', '99999']]
,'cod_auth':'aaaaa','status':'OPEN'}, {'nome_disciplina':'Engenharia de Software','cod_disciplina':'CIC002', 'turma':'B','data_aula':date(2023,5,10),'professor':'111111111', 'alunos_presentes':[['Aluno0', '00000'],
 ['Aluno1', '11111'],
 ['Aluno2', '22222'],
 ['Aluno3', '33333'],
 ['Aluno4', '44444'],
 ['Aluno5', '55555'],
 ['Aluno6', '66666'],
 ['Aluno7', '77777'],
 ['Aluno8', '88888'],
 ['Aluno9', '99999']]
,'cod_auth':'bbbbb','status':'OPEN'},{'nome_disciplina':'Calculo 2','cod_disciplina':'MAT001', 'turma':'A','data_aula':date(2023,5,15),'professor':'111111111', 'alunos_presentes':[['Aluno0', '00000'],
 ['Aluno1', '11111'],
 ['Aluno2', '22222'],
 ['Aluno3', '33333'],
 ['Aluno4', '44444'],
 ['Aluno5', '55555'],
 ['Aluno6', '66666'],
 ['Aluno7', '77777'],
 ['Aluno8', '88888'],
 ['Aluno9', '99999']]
,'cod_auth':'ccccc','status':'OPEN'}]
