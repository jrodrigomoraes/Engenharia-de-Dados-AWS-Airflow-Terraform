    SELECT d.nome nome, 
           v.modelo modelo, 
           CAST(month(f.data_locacao) AS VARCHAR) mes, 
           CAST(year(f.data_locacao) AS VARCHAR) ano,
           CAST(COUNT(*) AS VARCHAR) total
    FROM locadora_catalog.fato_locacoes f
    INNER JOIN locadora_catalog.dim_veiculos v
    ON f.veiculo_id = v.id_veiculo
    INNER JOIN locadora_catalog.dim_despachantes d
    ON f.despachante_id = d.id_despachante
    GROUP BY d.nome, v.modelo, month(f.data_locacao), year(f.data_locacao)
    ORDER BY total desc