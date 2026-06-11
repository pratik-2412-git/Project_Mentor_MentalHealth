import pandas as pd
import random
random.seed(42)

df = pd.read_csv('../data/labeled/Dataset_mentalhealth_clean.csv')

# ─────────────────────────────────────────────────────────────────────────────
# SMART RELABELING
# After manually inspecting all 172 records, these are the correct labels.
# Many "Positive" records were actually about Anxiety, Depression, or Neutral.
# ─────────────────────────────────────────────────────────────────────────────

correct_labels = {
    # ANXIETY - questions about anxiety disorders, panic, stress, trauma, OCD
    1:  'Anxiety',   # What is a panic attack?
    2:  'Anxiety',   # panic attack vs anxiety attack
    3:  'Anxiety',   # types of mental illness
    7:  'Anxiety',   # How to manage stress?
    8:  'Anxiety',   # family history - immune?
    9:  'Anxiety',   # Do children have mental health issues?
    12: 'Anxiety',   # What causes mental health problems?
    13: 'Anxiety',   # worried about my mental health
    14: 'Anxiety',   # How do I know if Im unwell?
    15: 'Anxiety',   # worried about friend or relative
    25: 'Anxiety',   # someone with symptoms of serious mental disorder
    26: 'Anxiety',   # warning signs of mental illness
    29: 'Anxiety',   # Psychological Factors - Mental Illness
    30: 'Anxiety',   # Environmental Factors - Mental Illness
    37: 'Anxiety',   # How does someone acquire a mental illness?
    51: 'Anxiety',   # Can mental health cause seizures?
    53: 'Anxiety',   # Who should I talk to about mental health?
    56: 'Anxiety',   # types treated by psychiatrist
    60: 'Anxiety',   # psychosis vs neurosis
    61: 'Anxiety',   # anxiety vs stress
    89: 'Anxiety',   # What Is Racial Trauma?
    90: 'Anxiety',   # How Does Racism Affect Your Physical Health?
    91: 'Anxiety',   # How to Deal With Racism and Racial Trauma?
    111:'Anxiety',   # Impact of Social Isolation on Mental Health
    115:'Anxiety',   # things that Affect Mental Health at Work
    116:'Anxiety',   # prevent Mental Health Issues in Workplace
    117:'Anxiety',   # How to Deal with Homesickness?
    122:'Anxiety',   # Dangers of Suppressed Anger
    123:'Anxiety',   # Steps to Help Manage My Anger
    138:'Anxiety',   # generalized anxiety disorder - families
    139:'Anxiety',   # treat children with anxiety disorders
    140:'Anxiety',   # learn about anxiety and mood disorders
    141:'Anxiety',   # What Is Post-Traumatic Stress Disorder?
    142:'Anxiety',   # Coping Factors for Stress
    143:'Anxiety',   # How to treat OCD?
    145:'Anxiety',   # substance use problem
    146:'Anxiety',   # help for alcohol or drug use
    147:'Anxiety',   # drinking too much
    149:'Anxiety',   # past difficulties - mental health condition
    150:'Anxiety',   # smoking/drinking affect mental health
    153:'Anxiety',   # traumatic childhood events - mental health
    162:'Anxiety',   # stigma surrounding mental health
    163:'Anxiety',   # coping strategies not working
    165:'Anxiety',   # sudden increase in panic attacks
    166:'Anxiety',   # financial hardships - stress and anxiety

    # DEPRESSION - questions about depression, suicide, hopelessness, isolation
    4:  'Depression', # What does mental-illness mean?
    23: 'Depression', # older person living alone - depressed
    39: 'Depression', # suicide vs homicide numbers
    40: 'Depression', # more died by suicide than homicide
    41: 'Depression', # 90% who attempt suicide had mental illness
    42: 'Depression', # resources for suicide prevention
    59: 'Depression', # How do I stop suicidal thoughts?
    62: 'Depression', # sadness vs depression
    85: 'Depression', # facts about Mental Health
    87: 'Depression', # major depressive disorder (MDD)
    92: 'Depression', # Depression Different in Older Adults?
    93: 'Depression', # Psychotic Depression vs Other Disorders
    94: 'Depression', # Symptoms of Psychotic Depression
    95: 'Depression', # Symptoms of Dysthymia
    96: 'Depression', # Depressive Disorder with Seasonal Pattern
    97: 'Depression', # What Causes Depression?
    98: 'Depression', # How Is Depression Diagnosed?
    99: 'Depression', # How Is Depression Treated?
    100:'Depression', # Outlook for People With Depression
    124:'Depression', # Do I Have Clinical Depression?
    125:'Depression', # feeling suicidal - what to do
    129:'Depression', # Depression Later In Life
    130:'Depression', # Efforts to Improve Treatment Of Depression
    131:'Depression', # Treatment-Resistant Depression
    132:'Depression', # risks of untreated depression
    133:'Depression', # psychiatric conditions co-exist with depression
    156:'Depression', # I am feeling lost
    158:'Depression', # losing motivation - how to regain
    164:'Depression', # isolated and lonely - build connections

    # NEUTRAL - factual/informational, no personal distress
    6:  'Neutral',   # patients with schizophrenia violent?
    10: 'Neutral',   # side effects of medication
    16: 'Neutral',   # deal with someone telling me what to do
    18: 'Neutral',   # What is substance abuse?
    27: 'Neutral',   # How common are mental illnesses?
    36: 'Neutral',   # ethnic/racial groups - mental illness
    49: 'Neutral',   # Is mental health genetic?
    54: 'Neutral',   # psychiatrist vs psychologist vs therapist
    55: 'Neutral',   # psychotherapy vs counselling
    58: 'Neutral',   # Can therapists prescribe medication?
    63: 'Neutral',   # How do you know if you have an addiction?
    64: 'Neutral',   # Are mental health problems common?
    73: 'Neutral',   # side effects of neurofeedback
    74: 'Neutral',   # neurofeedback vs biofeedback
    101:'Neutral',   # When a Child Needs Mental Health Assessment?
    105:'Neutral',   # Is Hypnotherapy Dangerous?
    106:'Neutral',   # Who Performs Hypnotherapy?
    119:'Neutral',   # Who Treats Mental Illness?
    126:'Neutral',   # Why is behavioral health important?
    127:'Neutral',   # similarities Mental and behavioral health
    144:'Neutral',   # evidence on vaping
    148:'Neutral',   # unhealthy relationship with food
    154:'Neutral',   # Why is womens mental health important?
    155:'Neutral',   # Hello, How are you?
    157:'Neutral',   # Bye
    167:'Neutral',   # What are you doing now?
    168:'Neutral',   # Who are you?
    169:'Neutral',   # helpline number suicide prevention India
    170:'Neutral',   # best mental health hospital New York
    171:'Neutral',   # best hypnotherapist London
    172:'Neutral',   # best psychiatrist Mumbai

    # POSITIVE - recovery, lifestyle, wellness, self-improvement
    5:  'Positive',  # How can you treat mental illness?
    11: 'Positive',  # Are there cures for mental health problems?
    17: 'Positive',  # Can you prevent mental health problems?
    19: 'Positive',  # addiction mental health specialist for relative
    20: 'Positive',  # Can I quit smoking on my own?
    21: 'Positive',  # How much alcohol is too much?
    22: 'Positive',  # Can addictions be cured?
    24: 'Positive',  # psychotherapy substitute for medication?
    28: 'Positive',  # can they ever get better again?
    31: 'Positive',  # get over mental illness without medication
    32: 'Positive',  # stabilize mental illness with medication
    33: 'Positive',  # why routine for mental illness
    34: 'Positive',  # just take meds and no therapy - safe?
    35: 'Positive',  # exercising help control mental illness
    38: 'Positive',  # Is mental illness a chronic disorder?
    43: 'Positive',  # medical coverage for mental health
    44: 'Positive',  # Therapy and self-help waste of time?
    45: 'Positive',  # Can I do anything for person with mental health issue?
    46: 'Positive',  # prevent a mental health condition
    47: 'Positive',  # Types Of Mental Health Treatment
    48: 'Positive',  # Find A Support Group
    50: 'Positive',  # mental health affect physical health
    52: 'Positive',  # mental health issues lead to addiction
    57: 'Positive',  # types of antidepressants
    65: 'Positive',  # help paying for medication
    66: 'Positive',  # feel better after medication - cured?
    67: 'Positive',  # before starting new medication
    68: 'Positive',  # involved in treatment - what to know
    69: 'Positive',  # find mental health professional for child
    70: 'Positive',  # Can people with mental illness recover?
    71: 'Positive',  # What happens in therapy session?
    72: 'Positive',  # How long in therapy?
    75: 'Positive',  # drink alcohol while taking antidepressants
    76: 'Positive',  # taking antidepressant - feel great
    77: 'Positive',  # medication sexual side effects
    78: 'Positive',  # Will I become addicted to medication?
    79: 'Positive',  # psychiatric medications cost
    80: 'Positive',  # long-term effects of medication
    81: 'Positive',  # relative stops taking medication
    82: 'Positive',  # recently prescribed antidepressant
    83: 'Positive',  # negative effects stopping antidepressants
    84: 'Positive',  # take medication rest of life
    86: 'Positive',  # What is insomnia disorder?
    88: 'Positive',  # Mental Health with Prostate Cancer
    102:'Positive',  # How Does Hypnotherapy Work?
    103:'Positive',  # Benefits of Hypnotherapy
    104:'Positive',  # Drawbacks of Hypnotherapy
    107:'Positive',  # Vitamins on Mental Health
    108:'Positive',  # Lack of Sleep Cause Mental Illness
    109:'Positive',  # Tips for Getting Better Sleep
    110:'Positive',  # Benefits of Journaling
    112:'Positive',  # cope with social isolation
    113:'Positive',  # Sports Help Mental Health
    114:'Positive',  # Negative Effects of Sports on Mental Health
    118:'Positive',  # Yoga to Improve Mental Health
    120:'Positive',  # benefits of listening to Music
    121:'Positive',  # Impact of Spirituality on Mental Health
    128:'Positive',  # eating habits for better mental health
    134:'Positive',  # What is self-management?
    135:'Positive',  # Is self-management right for me?
    136:'Positive',  # How do self-management courses work?
    137:'Positive',  # How can I find self-management course?
    151:'Positive',  # aging affect mental health
    152:'Positive',  # physical activity affect mental health
    159:'Positive',  # set realistic goals
    160:'Positive',  # resources or support groups
    161:'Positive',  # books or apps for mental health
}

# Apply correct labels
print("Applying corrected labels...")
df['label'] = df['record_id'].map(correct_labels).fillna(df['label'])

print("\nLabel distribution AFTER smart relabeling:")
print(df['label'].value_counts())

# ─────────────────────────────────────────────────────────────────────────────
# BALANCING - oversample minority classes to ~80 each
# ─────────────────────────────────────────────────────────────────────────────
print("\nBalancing classes to ~80 records each...")

TARGET = 80
balanced_dfs = []

for label in ['Anxiety', 'Depression', 'Neutral', 'Positive']:
    label_df = df[df['label'] == label].copy()
    current = len(label_df)
    
    if current < TARGET:
        # Oversample with replacement
        extra = label_df.sample(n=TARGET - current, replace=True, random_state=42)
        label_df = pd.concat([label_df, extra], ignore_index=True)
        print(f"  {label}: {current} → {len(label_df)} (oversampled +{TARGET-current})")
    elif current > TARGET:
        # Undersample
        label_df = label_df.sample(n=TARGET, random_state=42)
        print(f"  {label}: {current} → {len(label_df)} (undersampled)")
    else:
        print(f"  {label}: {current} → {len(label_df)} (unchanged)")
    
    balanced_dfs.append(label_df)

balanced_df = pd.concat(balanced_dfs, ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
balanced_df['record_id'] = range(1, len(balanced_df) + 1)

print(f"\nFinal balanced distribution:")
print(balanced_df['label'].value_counts())
print(f"Total records: {len(balanced_df)}")

# Save both
df.to_csv('../data/labeled/Dataset_mentalhealth_clean.csv', index=False)
balanced_df.to_csv('../data/labeled/mental_health_qa_balanced.csv', index=False)

print("\n" + "="*60)
print("✅ DONE!")
print("="*60)
print("  ✓ Dataset_mentalhealth_clean.csv  → relabeled base (172 records)")
print("  ✓ mental_health_qa_balanced.csv   → balanced training set (320 records)")
print("\nNext step → DistilBERT fine-tuning!")
