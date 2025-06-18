    SELECT cli.nome AS nome, CAST(COUNT(*) AS VARCHAR) AS total
    FROM locadora_catalog.fato_locacoes f
    INNER JOIN locadora_catalog.dim_clientes cli
      ON f.cliente_id = cli.id_cliente
    GROUP BY cli.nome
    ORDER BY total DESC