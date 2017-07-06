#---------------------------------------------------------------------- 
# hero_dict is a dictionary whose keys are hero_id_tags and whose 
# values are in-game category tags describing attributes of heroes
# 
# tags '1','2','3' = indicators difficulty of play 
# tags 'female', 'male', 'neuter' = presented gender of hero
# tags 'agi', 'int', 'str' = main attribute hero uses 
# the other tags mark in-gagme categories of relevence 
# 
# except for difficulty level and gender and main attribute, tags are not (usually) mutually  
# exclusive and are not used uniformly or exuaustively across heroes
#---------------------------------------------------------------------- 


# h_tags is a list of tags
h_tags = ['1', '2', '3', 
          'female', 'male', 'neuter',
          'agi', 'int', 'str',
          'carry', 'disabler', 'durable', 'escape', 'initiator',  
          'jungler',  'melee',  'nuker', 'pusher', 'ranged', 'support']

hero_dict = {}
hero_dict['npc_dota_hero_antimage'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', '1']
hero_dict['npc_dota_hero_axe'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'jungler']
hero_dict['npc_dota_hero_bane'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'durable', '2']
hero_dict['npc_dota_hero_bloodseeker'] = ['male', 'melee', 'agi', 'carry', 'disabler', 'nuker', 'jungler', 'initiator', '1']
hero_dict['npc_dota_hero_crystal_maiden'] = ['female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'jungler', '1']
hero_dict['npc_dota_hero_drow_ranger'] = ['female', 'ranged', 'agi', 'carry', 'disabler', 'pusher', '1']
hero_dict['npc_dota_hero_earthshaker'] = ['male', 'melee', 'str', 'initiator', 'support', 'disabler', 'nuker']
hero_dict['npc_dota_hero_juggernaut'] = ['male', 'melee', 'agi', 'carry', 'pusher', 'escape', '1']
hero_dict['npc_dota_hero_mirana'] = ['female', 'ranged', 'agi', 'carry', 'escape', 'nuker', 'support', 'disabler', '2']
hero_dict['npc_dota_hero_nevermore'] = ['male', 'ranged', 'agi', 'carry', 'nuker', '2']
hero_dict['npc_dota_hero_morphling'] = ['male', 'ranged', 'agi', 'carry', 'escape', 'nuker', 'durable', 'disabler', '3']
hero_dict['npc_dota_hero_phantom_lancer'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'pusher', '2']
hero_dict['npc_dota_hero_puck'] = ['female', 'ranged', 'int', 'initiator', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_pudge'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_razor'] = ['male', 'ranged', 'agi', 'carry', 'durable', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_sand_king'] = ['male', 'melee', 'str', 'initiator', 'escape', 'disabler', 'nuker', 'jungler']
hero_dict['npc_dota_hero_storm_spirit'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'initiator', 'escape', '3']
hero_dict['npc_dota_hero_sven'] = ['male', 'melee', 'str', 'carry', 'durable', 'disabler', 'initiator', 'nuker']
hero_dict['npc_dota_hero_tiny'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'pusher', 'durable']
hero_dict['npc_dota_hero_vengefulspirit'] = ['female', 'ranged', 'agi', 'support', 'escape', 'nuker', 'initiator', 'disabler', '1']
hero_dict['npc_dota_hero_windrunner'] = ['female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_zuus'] = ['male', 'ranged', 'int', 'nuker', '1']
hero_dict['npc_dota_hero_kunkka'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_lina'] = ['female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', '1']
hero_dict['npc_dota_hero_lich'] = ['male', 'ranged', 'int', 'support', 'nuker', '1']
hero_dict['npc_dota_hero_lion'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '1']
hero_dict['npc_dota_hero_shadow_shaman'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', 'initiator', '1']
hero_dict['npc_dota_hero_slardar'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'escape']
hero_dict['npc_dota_hero_tidehunter'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_witch_doctor'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_riki'] = ['male', 'melee', 'agi', 'carry', 'escape', 'disabler', '1']
hero_dict['npc_dota_hero_enigma'] = ['male', 'ranged', 'int', 'pusher', 'disabler', 'initiator', 'jungler', '2']
hero_dict['npc_dota_hero_tinker'] = ['male', 'ranged', 'int', 'carry', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_sniper'] = ['male', 'ranged', 'agi', 'carry', 'nuker', '1']
hero_dict['npc_dota_hero_necrolyte'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'durable', '1']
hero_dict['npc_dota_hero_warlock'] = ['male', 'ranged', 'int', 'support', 'disabler', 'initiator', '1']
hero_dict['npc_dota_hero_beastmaster'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_queenofpain'] = ['female', 'ranged', 'int', 'carry', 'escape', 'nuker', '2']
hero_dict['npc_dota_hero_venomancer'] = ['male', 'ranged', 'agi', 'support', 'initiator', 'nuker', 'pusher', 'disabler', '1']
hero_dict['npc_dota_hero_faceless_void'] = ['male', 'melee', 'agi', 'carry', 'escape', 'initiator', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_skeleton_king'] = ['male', 'melee', 'str', 'initiator', 'support', 'disabler', 'durable', 'carry']
hero_dict['npc_dota_hero_death_prophet'] = ['female', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_phantom_assassin'] = ['female', 'melee', 'agi', 'carry', 'escape', '1']
hero_dict['npc_dota_hero_pugna'] = ['male', 'ranged', 'int', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_templar_assassin'] = ['female', 'ranged', 'agi', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_viper'] = ['male', 'ranged', 'agi', 'carry', 'durable', 'initiator', 'disabler', '1']
hero_dict['npc_dota_hero_luna'] = ['female', 'ranged', 'agi', 'carry', 'pusher', 'nuker', '1']
hero_dict['npc_dota_hero_dragon_knight'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable', 'pusher']
hero_dict['npc_dota_hero_dazzle'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_rattletrap'] = ['male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_leshrac'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'support', 'pusher', '1']
hero_dict['npc_dota_hero_furion'] = ['male', 'ranged', 'int', 'carry', 'escape', 'nuker', 'jungler', 'pusher', '2']
hero_dict['npc_dota_hero_life_stealer'] = ['male', 'melee', 'str', 'durable', 'jungler', 'disabler', 'carry', 'escape']
hero_dict['npc_dota_hero_dark_seer'] = ['male', 'ranged', 'int', 'initiator', 'disabler', 'escape', 'jungler', '2']
hero_dict['npc_dota_hero_clinkz'] = ['male', 'ranged', 'agi', 'carry', 'escape', 'pusher', '2']
hero_dict['npc_dota_hero_omniknight'] = ['male', 'melee', 'str', 'durable', 'support', 'nuker']
hero_dict['npc_dota_hero_enchantress'] = ['female', 'ranged', 'int', 'support', 'disabler', 'pusher', 'jungler', 'durable', '2']
hero_dict['npc_dota_hero_huskar'] = ['male', 'ranged', 'str', 'initiator', 'carry', 'durable']
hero_dict['npc_dota_hero_night_stalker'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_broodmother'] = ['female', 'melee', 'agi', 'carry', 'escape', 'nuker', 'pusher', '2']
hero_dict['npc_dota_hero_bounty_hunter'] = ['male', 'melee', 'agi', 'escape', 'nuker', '1']
hero_dict['npc_dota_hero_weaver'] = ['male', 'ranged', 'agi', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_jakiro'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_batrider'] = ['male', 'ranged', 'int', 'initiator', 'disabler', 'escape', 'jungler', '2']
hero_dict['npc_dota_hero_chen'] = ['male', 'ranged', 'int', 'support', 'pusher', 'jungler', '3']
hero_dict['npc_dota_hero_spectre'] = ['female', 'melee', 'agi', 'carry', 'escape', 'durable', '2']
hero_dict['npc_dota_hero_doom_bringer'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_ancient_apparition'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_ursa'] = ['male', 'melee', 'agi', 'carry', 'jungler', 'durable', 'disabler', '1']
hero_dict['npc_dota_hero_spirit_breaker'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'escape']
hero_dict['npc_dota_hero_gyrocopter'] = ['male', 'ranged', 'agi', 'carry', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_alchemist'] = ['male', 'melee', 'str', 'initiator', 'support', 'disabler', 'nuker', 'carry', 'durable']
hero_dict['npc_dota_hero_invoker'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'escape', 'pusher', '3']
hero_dict['npc_dota_hero_silencer'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', 'initiator', '2']
hero_dict['npc_dota_hero_obsidian_destroyer'] = ['male', 'ranged', 'int', 'carry', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_lycan'] = ['male', 'melee', 'str', 'carry', 'pusher', 'jungler', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_brewmaster'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_shadow_demon'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '2']
hero_dict['npc_dota_hero_lone_druid'] = ['male', 'ranged', 'agi', 'carry', 'pusher', 'jungler', 'durable', '3']
hero_dict['npc_dota_hero_meepo'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', 'initiator', 'pusher', '3']
hero_dict['npc_dota_hero_keeper_of_the_light'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'jungler', '2']
hero_dict['npc_dota_hero_visage'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', 'durable', '3']
hero_dict['npc_dota_hero_disruptor'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '2']
hero_dict['npc_dota_hero_rubick'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '3']
hero_dict['npc_dota_hero_ogre_magi'] = ['male', 'melee', 'int', 'support', 'disabler', 'nuker', 'durable', 'initiator', '1']
hero_dict['npc_dota_hero_nyx_assassin'] = ['male', 'melee', 'agi', 'disabler', 'initiator', 'escape', 'nuker', '2']
hero_dict['npc_dota_hero_naga_siren'] = ['female', 'melee', 'agi', 'carry', 'escape', 'support', 'pusher', 'disabler', 'initiator', '2']
hero_dict['npc_dota_hero_undying'] = ['male', 'melee', 'str', 'nuker', 'support', 'disabler', 'durable', '1']
hero_dict['npc_dota_hero_chaos_knight'] = ['male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'pusher', '1']
hero_dict['npc_dota_hero_wisp'] = ['neuter', 'ranged', 'str', 'escape', 'support', 'nuker', '3']
hero_dict['npc_dota_hero_treant'] = ['male', 'melee', 'str', 'initiator', 'support', 'disabler', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_magnataur'] = ['male', 'melee', 'str', 'initiator', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_centaur'] = ['male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', 'escape', '1']
hero_dict['npc_dota_hero_slark'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', '1']
hero_dict['npc_dota_hero_shredder'] = ['male', 'melee', 'str', 'nuker', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_medusa'] = ['female', 'ranged', 'agi', 'carry', 'disabler', 'durable', '1']
hero_dict['npc_dota_hero_troll_warlord'] = ['male', 'ranged', 'agi', 'carry', 'pusher', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_techies'] = ['male', 'ranged', 'int', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_abaddon'] = ['male', 'melee', 'str', 'carry', 'support', 'durable', '1']
hero_dict['npc_dota_hero_bristleback'] = ['male', 'melee', 'str', 'initiator', 'carry', 'nuker', 'durable', '1']
hero_dict['npc_dota_hero_abyssal_underlord'] = ['male', 'melee', 'str', 'support', 'disabler', 'nuker', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_legion_commander'] = ['female', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'nuker', '1']
hero_dict['npc_dota_hero_earth_spirit'] = ['male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', 'escape', '3']
hero_dict['npc_dota_hero_arc_warden'] = ['neuter', 'ranged', 'agi', 'carry', 'escape', 'nuker', '3']
hero_dict['npc_dota_hero_elder_titan'] = ['male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_tusk'] = ['male', 'melee', 'str', 'initiator', 'nuker', 'disabler', '2']
hero_dict['npc_dota_hero_winter_wyvern'] = ['female', 'ranged', 'int', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_ember_spirit'] = ['male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', 'initiator', '2']
hero_dict['npc_dota_hero_oracle'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'escape', '3']
hero_dict['npc_dota_hero_phoenix'] = ['neuter', 'ranged', 'str', 'initiator', 'support', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_skywrath_mage'] = ['male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_terrorblade'] = ['male', 'melee', 'agi', 'carry', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_monkey_king'] = ['male', 'melee', 'agi', 'initiator', 'carry', 'escape', 'disabler', '2']


#---------------------------------------------------------------------- 
# tag_dict is a dictionary whose keys are tags and whose 
# values are lists of heroes that are marked with that tag
#---------------------------------------------------------------------- 

tag_dict = {}
length_by_tag = {}
chats_by_tag = {}

for t in h_tags:
  tag_dict[t] = []
  for (h,tag_list) in list(hero_dict.items()):
    if t in tag_list:
      tag_dict[t] += [h]

      