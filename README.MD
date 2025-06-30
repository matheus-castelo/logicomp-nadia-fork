# logicomp-nadia-fork

Implementação de regras de lógica no NADIA, desenvolvida inicialmente no PyCharm e posteriormente adaptada para execução no Google Colab.

---

## 📖 Descrição

Este projeto consiste na formalização, em NADIA, das seguintes regras de inferência:

1. **Leis de De Morgan** (quatro variações):
   - ¬(A ∧ B) ⊢ ¬A ∨ ¬B  
   - ¬(A ∨ B) ⊢ ¬A ∧ ¬B  
   - ¬A ∨ ¬B ⊢ ¬(A ∧ B)  
   - ¬A ∧ ¬B ⊢ ¬(A ∨ B)  

2. **Contraposição**:
   - A → B ⊢ ¬B → ¬A  

3. **Silogismo Disjuntivo** (duas variações):
   - A ∨ B, ¬B ⊢ A  
   - A ∨ B, ¬A ⊢ B  

---

## ⚙️ Pré‑requisitos

- Python 3.7+
- Google Colab (ou ambiente local com Jupyter)
- Biblioteca RPLY
- IPyWidgets (apenas no Colab)

---

## 🚀 Como Executar no Google Colab

1. **Clone o repositório**  
   ```bash
   !git clone https://github.com/matheus-castelo/logicomp-nadia-fork
   ```

2. **Instale os requisitos**

   ```bash
   !pip install rply ipywidgets
   ```

3. **Configure o `sys.path` e importe o `check_proof`**

   ```python
   import sys
   sys.path.append('/content/logicomp-nadia-fork/src')

   from nadia.nadia_pt_fo import check_proof
   ```

4. **Use o `check_proof`**

```python
# Exemplo
from nadia.nadia_pt_fo import check_proof

print(check_proof('''1. A|B              pre
2. A->C             pre
3. B->C             pre
4. {    A           hip
5.      C           ->e 4,2
   } 
6. {    B           hip
7.      C           ->e 6,3
   }
8. C                |e 1, 4-5, 6-7'''))
```

---

## 📁 Estrutura do Repositório

```text
content/
└── logicomp-nadia-fork/
    ├── src/
    │   └── nadia/
    │       ├── __init__.py
    │       ├── nadia_pt_fo.py    # Onde o `check_proof` está definido
    │       └── … (outros módulos)
    └── README.md
```

> **Nota:** Se você não adicionar o caminho `/content/logicomp-nadia-fork/src` ao `sys.path`, o Python carregará a instalação padrão do NADIA ao invés desta versão customizada.

---

## 🔗 Links Úteis

* **Código‑Fonte (Google Drive)**
  [https://drive.google.com/drive/folders/1u3\_bdYKhEHu8YmxL-UALQ6ePeQImtRHn?usp=sharing](https://drive.google.com/drive/folders/1u3_bdYKhEHu8YmxL-UALQ6ePeQImtRHn?usp=sharing)

* **Slides / Apresentação**
  [https://drive.google.com/drive/folders/1u3\_bdYKhEHu8YmxL-UALQ6ePeQImtRHn?usp=sharing](https://drive.google.com/drive/folders/1u3_bdYKhEHu8YmxL-UALQ6ePeQImtRHn?usp=sharing)

* **Colab da Apresentação**
  [https://drive.google.com/drive/folders/1F6GTl\_C-K7NutJaLBCWKo-d6qWjiIEyR?usp=sharing](https://drive.google.com/drive/folders/1F6GTl_C-K7NutJaLBCWKo-d6qWjiIEyR?usp=sharing)

---

## ✅ Casos de Testes:
### - UTILIZANDO AS REGRAS
```python
from nadia.nadia_pt_fo import check_proof

print("# DE MORGAN 1: ¬(A ∨ B) ⊢ ¬A ∧ ¬B")
print(check_proof('''
# ~(A|B) |- ~A&~B
1. ~(A|B)          pre
2. ~A&~B           demorgan2 1
'''))

print("# DE MORGAN 2: ¬A ∧ ¬B ⊢ ¬(A ∨ B)")
print(check_proof('''
# ~(A&B) |- ~A|~B
1. ~(A&B)          pre
2. ~A|~B           demorgan1 1
'''))


print("# DE MORGAN 4: ¬A ∨ ¬B ⊢ ¬(A ∧ B)")
print(check_proof('''
# ~A|~B |- ~(A&B)
1. ~A|~B           pre
2. ~(A&B)          demorgan3 1
'''))

print("# DE MORGAN 3: ¬(A ∧ B) ⊢ ¬A ∨ ¬B")
print(check_proof('''
# ~A&~B |- ~(A|B)
1. ~A&~B           pre
2. ~(A|B)          demorgan4 1
'''))

print("# CONTRAPOSIÇÃO: A → B ⊢ ¬B → ¬A")
print(check_proof('''
# (A->B) |- (~B->~A)
1. A->B            pre
2. ~B->~A          contrapositive 1
'''))

print("# SILOGISMO DISJUNTIVO 1: A ∨ B, ¬B ⊢ A")
print(check_proof('''
# (A|B), ~B |- A
1. A|B             pre
2. ~B              pre
3. A               disj_syllogism 1,2
'''))

print("# SILOGISMO DISJUNTIVO 2: A ∨ B, ¬A ⊢ B")
print(check_proof('''
# (A|B), ~A |- B
1. A|B             pre
2. ~A              pre
3. B               disj_syllogism 1,2
'''))
```
### SEM UTILIZAR AS REGRAS
```python
from nadia.nadia_pt_fo import check_proof

# DE MORGAN 1: ¬(A ∨ B) ⊢ ¬A ∧ ¬B
print("# DE MORGAN 1: ¬(A ∨ B) ⊢ ¬A ∧ ¬B")
print(check_proof('''
# ~(A|B) |- ~A&~B
1. ~(A|B)    pre
2. {    A    hip
3.    A|B    |i 2
4.    @    ~e 1,3
   }
5. ~A    ~i 2-4
6. {    B    hip
7.    A|B    |i 6
8.    @    ~e 1,7
   }
9. ~B    ~i 6-8
10. ~A&~B    &i 5,9
'''))

# DE MORGAN 2: ¬A ∧ ¬B ⊢ ¬(A ∨ B)
print("# DE MORGAN 2: ¬A ∧ ¬B ⊢ ¬(A ∨ B)")
print(check_proof('''
# ~A&~B |- ~(A|B)
1. ~A&~B    pre
2. {    A|B    hip
3.    {    A    hip
4.    ~A    &e 1
5.    @    ~e 4,3
    }
6.    {    B    hip
7.    ~B    &e 1
8.    @    ~e 7,6
    }
9.    @    |e 2, 3-5, 6-8
    }
10. ~(A|B)    ~i 2-9
'''))

# DE MORGAN 3: ¬(A ∧ B) ⊢ ¬A ∨ ¬B
print("# DE MORGAN 3: ¬(A ∧ B) ⊢ ¬A ∨ ¬B")
print(check_proof('''
# ~(A&B) |- ~A|~B
1. ~(A&B)    pre
2. {    ~(~A|~B)    hip
3.    {    ~A    hip
4.        ~A|~B    |i 3
5.        @    ~e 2,4
       }
6.    A    raa 3-5
7.    {    ~B    hip
8.        ~A|~B    |i 7
9.        @    ~e 2,8
       }
10.   B    raa 7-9
11.   A&B    &i 6,10
12.   @    ~e 1,11
    }
13. ~A|~B    raa 2-12
'''))

# DE MORGAN 4: ¬A ∨ ¬B ⊢ ¬(A ∧ B)
print("# DE MORGAN 4: ¬A ∨ ¬B ⊢ ¬(A ∧ B)")
print(check_proof('''
# ~A|~B |- ~(A&B)
1. ~A|~B    pre
2. {    A&B    hip
3.    A    &e 2
4.    B    &e 2
5.    {    ~A    hip
6.        @    ~e 3,5
       }
7.    {    ~B    hip
8.        @    ~e 4,7
       }
9.    @    |e 1, 5-6, 7-8
    }
10. ~(A&B)    ~i 2-9
'''))

# CONTRAPOSIÇÃO: A → B ⊢ ¬B → ¬A
print("# CONTRAPOSIÇÃO: A → B ⊢ ¬B → ¬A")
print(check_proof('''
# A->B |- ~B->~A
1. A->B    pre
2. {    ~B    hip
3.    {    A    hip
4.        B    ->e 1,3
5.        @    ~e 2,4
       }
6.    ~A    ~i 3-5
    }
7. ~B->~A    ->i 2-6
'''))

# SILOGISMO DISJUNTIVO 1: A ∨ B, ¬B ⊢ A
print("# SILOGISMO DISJUNTIVO 1: A ∨ B, ¬B ⊢ A")
print(check_proof('''
# A|B, ~B |- A
1. A|B    pre
2. ~B    pre
3. {    A    hip
   }
4. {    B    hip
5.    @    ~e 4,2
6.    A    @e 5
   }
7. A    |e 1, 3-3,4-6
'''))

# SILOGISMO DISJUNTIVO 2: A ∨ B, ¬A ⊢ B
print("# SILOGISMO DISJUNTIVO 2: A ∨ B, ¬A ⊢ B")
print(check_proof('''
# A|B, ~A |- B
1. A|B    pre
2. ~A     pre
3. {    A    hip
4.    @    ~e 3,2
5.    B    @e 4
   }
6. {    B    hip
   }
7. B     |e 1, 3-5,6-6
'''))

```


## 📝 Observações

> Este repositório não segue um fluxo de commits convencional, pois as primeiras versões apresentaram diversos erros e foram corrigidas ao longo do desenvolvimento.

---

*Desenvolvido por Matheus Castelo*

