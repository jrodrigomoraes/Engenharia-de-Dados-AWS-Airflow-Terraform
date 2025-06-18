    SELECT cli.nome AS nome,
           CAST(MONTH(f.data_locacao) AS VARCHAR) AS mes,
           CAST(YEAR(f.data_locacao) AS VARCHAR) AS ano,
           CAST(count(*) AS VARCHAR) AS total
    FROM locadora_catalog.fato_locacoes f
    INNER JOIN locadora_catalog.dim_clientes cli
    ON f.cliente_id = cli.id_cliente
    GROUP BY cli.nome, month(f.data_locacao), year(f.data_locacao)
    ORDER BY nome