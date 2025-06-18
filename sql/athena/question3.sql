    SELECT CAST(month(f.data_locacao) AS VARCHAR) AS mes,
           CAST(YEAR(f.data_locacao) AS VARCHAR) AS ano,
           CAST(ROUND(SUM(valor_total), 2) AS VARCHAR) AS total
    FROM locadora_catalog.fato_locacoes f
    GROUP BY month(f.data_locacao), year(f.data_locacao)
    ORDER BY mes, ano