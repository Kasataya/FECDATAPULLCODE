endpoints = [
        #candidate
                                                                        #'candidate/{candidate_id}/',
                                                                        #'candidate/{candidate_id}/history/',
                                                                        #'candidate/{candidate_id}/history/{cycle}/',
                                                                        #'candidate/{candidate_id}/totals/',
        'candidates/',#50163_rows CopyOFOtherTables
        #'candidates/search/',#50163_rows CopyOFOtherTables
        #'candidates/totals/',#72381_rows
        #'candidates/totals/aggregates/',#34_rows
                                                                        #'committee/{committee_id}/candidates/',
                                                                        #'committee/{committee_id}/candidates/history/',
                                                                        #'committee/{committee_id}/candidates/history/{cycle}',
        #committee
                                                                        #'candidate/{candidate_id}/committees/',
                                                                        #'candidate/{candidate_id}/committees/history/',
                                                                        #'candidate/{candidate_id}/committees/history/{cycle}/',
                                                                        #'candidate/{candidate_id}/',
                                                                        #'candidate/{candidate_id}/history/',
                                                                        #'candidate/{candidate_id}/history/{cycle}/',
        "committees/",#81696_rows
        #dates
        "calendar-dates/",#7496_rows
#        'calendar_datas/export/',######Issue with data import due to data types within columns (fix later) Requires a certain python libarary
        "election-dates/",#3198_rows
        "reporting-dates/",#4496_rows
        #financial
                                                                        #'committee/{committee_id}/reports/',
                                                                        #'committee/{committee_id}/totals/',
        #'elections/',               #Skipped
        #'elections/search/',#21233
        #'elections/summary/',       #Skipped
                                                                        #'reports/{entity_type}/',
        #'totals/by_entity/',        #Skipped
        #'totals/inaugural_committees/by_contributor/',#45825_rows
                                                                        #'totals/{by_entity_type}',
        #search
        #'names/candidates/',        #Skipped
        #'names/committees/',        #Skipped
        #filings
                                                                        #'candidate/{candidate_id}/filings/',
                                                                        #'candidate/{committee_id}/filings/',
        #'filings/',#502999
        #'operations-log/',#above 1.2 million records
        #receipts
        #'schedules/schedule_a/',    #Skipped
        #'schedules/schedule_a/by_imployer/',  #Skipped
        #'schedules/schedule_a/by_occupation/',
        #'schedules/schedule_a/by_size/',
        #'schedules/schedule_a/by_size/by_candidate/', #Skipped
        #'schedules/schedule_a/by_state/',
        #'schedules/schedule_a/by_state/by_candidate/', #Skipped
        #'schedules/schedule_a/by_state/by_candidate/totals/', #Skipped
        #'schedules/schedule_a/by_state/totals/',
        #'schedules/schedule_a/by_zip/',
        #'schedules/schedule_a/efile/',
                                                                        #'schedules/schedule_a/{sub_id}/',
        #disbursements
        #'schedules/schedule_b/',
        #'schedules/schedule_b/by_purpose/',
        #'schedules/schedule_b/by_recipient/',
        #'schedules/schedule_b/by_recipient_id/',
        #'schedules/schedule_b/efile/',
                                                                        #'schedules/schedule_b/{sub_id}/',
        #'schedules/schedule_h4/',
        #'schedules/schedule_h4/efile/',
        #loans
        #'schedules/schedule_c/',
                                                                        #'schedules/schedule_c/{sub_id}/',
        #debts
        #'schedules/schedule_d/',
                                                                        #'schedules/schedule_d/{sub_id}/',
        #independent expenditures
        #'schedules/schedule_e/',
        #'schedules/schedule_e/by_candidate', #skipped
        #'schedules/schedule_e/efile/',
        #'schedules/schedule_e/totals/by_candidate/',
        #party-coordinated expenditures
        #'schedules/schedule_f/',
                                                                        #'schedules/schedule_f/{sub_id}/',
        #communication cost
        #'communication_costs/',
        #'communication_costs/aggregates/',
        #'communication_costs/by_candidate/', #skipped
        #'communication_costs/totals/by_candidate/',
        #electioneering
        #'electioneering/',
        #'electioneering/aggregates/',
        #'electioneering/by_candidate/', #Skipped
        #'electioneering/totals/by_candidate/',
        #predidential
        #'presidential/contributions/by_candidate/',
        #'presidential/contributions/by_size/',
        #'presidential/contributions/by_state/',
        #'presidential/coverage_end_date/',
        #'presidential/financial_summary',
        #filer resources
        #"rad-analyst/",                              #14356
        #"state-election-office/", #skipped
        #national party accounts
        #"national_party/schedule_a/",               #61550
        #"national_party/schedule_b/",               #12731
        #efiling
        #'efile/filings/',
        #'efile/form1/',
        #'efile/form2/',
#        'efile/reports/house-senate/', #Not fully sure why an error accures whenever pulling this table
#        'efile/reports/pac-party/', #Not fully sure why an error accures whenever pulling this table
#        'efile/reports/presidential/', #Not fully sure why an error accures whenever pulling this table
        #audit
        #"audit-case/",                               #1063
        #"audit-category/",                           #14
        #"audit-primary-category",                   #14
        #"names/audit_candidates/", #Skipped
        #"names/audit_committees/", #Skipped
        #legal
        #"legal/search/" #Skipped
        ]  

