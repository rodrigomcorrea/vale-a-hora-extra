# Vale a hora extra?

Marque no calendário os dias em que pretende fazer hora extra e veja quanto realmente sobra no próximo holerite depois do INSS e do Imposto de Renda (tabelas de 2026, com a redução da Lei 15.270/2025).

Site: https://rodrigomcorrea.github.io/vale-a-hora-extra/

- Tudo é calculado no próprio navegador. Salário e dias marcados ficam salvos só no aparelho de quem usa.
- No celular, abra o site e use "Adicionar à Tela de Início" para usar como app.

## Como atualizar

`index.html` é a fonte. Depois de editar, gere o site e envie:

```bash
python build.py
```

## Dados

- Cidades e coordenadas: [kelvins/municipios-brasileiros](https://github.com/kelvins/municipios-brasileiros) (MIT)
- Feriados municipais: [joaopbini/feriados-brasil](https://github.com/joaopbini/feriados-brasil) (MIT), base de 2026

É uma estimativa: confira sempre com o holerite e com a convenção coletiva da sua categoria.
