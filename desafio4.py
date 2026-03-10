#SELECT 
#    c.id_cliente,
#    c.razao_social,
#    t.numero AS telefone
#FROM clientes c
#JOIN estados e ON c.id_estado = e.id_estado
#JOIN telefones t ON t.id_cliente = c.id_cliente
#WHERE e.sigla = 'SP';
