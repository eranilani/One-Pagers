import pandas as pd 

# For one
def get_info(ent_id, entities, entities_performances, entities_pieces, entities_skills, mediamentions, 
             wikipedia_pv, biographies, alt_names, include_lists = False) : 
    
    # Variable
    infos = ['id', 'name', 'gender', 'alive', 'birth_date', 'death_date', 'current_influence_percentile']
    entity = entities[entities.id == ent_id].loc[:, infos]
    
    # Standard 
    perf_list = entities_performances[entities_performances.entity_id == ent_id].performance_id.to_list()
    pieces_list = entities_pieces[entities_pieces.entity_id == ent_id].piece_id.to_list()
    skills_list = entities_skills[entities_skills.entity_id == ent_id].skill_id.to_list()
    mm_list = mediamentions[mediamentions.entity_id == ent_id].id.to_list()
    wiki_pv = wikipedia_pv[wikipedia_pv.entity_id == ent_id].id.to_list()
    bios_list = biographies[biographies.entity_id == ent_id].id.to_list()
    alter_names_list = alt_names[alt_names.entity_id == ent_id].name.to_list()
    
    # Getting number od occurences 
    entity['nb_perf'] = len(perf_list)
    entity['nb_pieces'] = len(pieces_list)
    entity['nb_media_mentions'] = len(mm_list)
    entity['nb_skills'] = len(skills_list)
    entity['nb_alt_names'] = len(alter_names_list)
    entity['nb_biographies'] = len(bios_list)
    
    # Getting list for easier access
    if include_lists : 
        entity['perf_list'] = entity.id.apply(lambda x : {ent_id : perf_list}[x])
        entity['pieces_list'] = entity.id.apply(lambda x : {ent_id : pieces_list}[x])
        entity['media_mentions'] = entity.id.apply(lambda x : {ent_id : mm_list}[x])
        entity['wiki_pv'] = entity.id.apply(lambda x : {ent_id : wiki_pv}[x])
        entity['skills_list'] = entity.id.apply(lambda x : {ent_id : skills_list}[x])
        entity['alter_names'] = entity.id.apply(lambda x : {ent_id : alter_names_list}[x])
        entity['bios_list'] = entity.id.apply(lambda x : {ent_id : bios_list}[x])
    
    return entity

# For lists 
def get_info_for_list(id_list) : 
    
    # Creating table 
    infos = ['id', 'name', 'gender', 'alive', 'birth_date', 'death_date', 'current_influence_percentile']
    df_info = entities[entities.id.apply(lambda x: x in id_list)].loc[:, infos]
    
    # Variables 
    keys = id_list
    perf_list, pieces_list, skills, mm_list, wiki_pv, bios, alter = [], [], [], [], [], [], []
    
    # Getting infos
    for ent_id in id_list : 
        perf_list.append(entities_performances[entities_performances.entity_id == ent_id].performance_id.to_list())
        pieces_list.append(entities_pieces[entities_pieces.entity_id == ent_id].piece_id.to_list())
        skills.append(entities_skills[entities_skills.entity_id == ent_id].skill_id.to_list())
        mm_list.append(mediamentions[mediamentions.entity_id == ent_id].id.to_list())
        wiki_pv.append(wikipedia_pv[wikipedia_pv.entity_id == ent_id].id.to_list())
        bios.append(biographies[biographies.entity_id == ent_id].id.to_list())
        alter.append(alt_names[alt_names.entity_id == ent_id].name.to_list())

    # Creating dict to include array in cells 
    perf_dico = dict(zip(keys, perf_list))
    pieces_dico = dict(zip(keys, pieces_list))
    skills_dico = dict(zip(keys, skills_list))
    mm_dico = dict(zip(keys, mm_list))
    wiki_dico = dict(zip(keys, wiki_pv))
    bios_dico = dict(zip(keys, bios))
    alter_dico = dict(zip(keys, alter))

    # Include lists in table for easier access
    df_info['perf_list'] = df_info.id.apply(lambda x : perf_dico[x])
    df_info['pieces_list'] = df_info.id.apply(lambda x : pieces_dico[x])
    df_info['skills_list'] = df_info.id.apply(lambda x : skills_dico[x])
    df_info['mm_list'] = df_info.id.apply(lambda x : mm_dico[x])    
    df_info['wiki_pv'] = df_info.id.apply(lambda x : wiki_dico[x])
    df_info['bios_list'] = df_info.id.apply(lambda x : bios_dico[x])
    df_info['alternames_list'] = df_info.id.apply(lambda x : alter_dico[x])
         
    return  df_info
    