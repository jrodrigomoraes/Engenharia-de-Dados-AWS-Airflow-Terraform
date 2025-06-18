    SELECT v.modelo, 
           CAST(YEAR(f.data_locacao) AS VARCHAR) as ano,
           CAST(MONTH(f.data_locacao) AS VARCHAR) as mes,
           CAST(count(*) AS VARCHAR) as total
    FROM locadora_catalog.fato_locacoes f
    INNER JOIN locadora_catalog.dim_veiculos v
        ON f.veiculo_id = v.id_veiculo
    GROUP BY v.modelo, MONTH(f.data_locacao), YEAR(f.data_locacao)
    ORDER BY total DESC