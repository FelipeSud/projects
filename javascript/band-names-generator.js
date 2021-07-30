// Random Band Names Generator
//Using a loop inside another loop (nested loop) to help generate new band name ideas.

for (var adj of [
    'Developer',
    'Helaman',
    'Mormon',
    'Ether',
    'Nephi'
]){
    for (var noun of [
        'Lamanites',
        'Missionaries',
        'Teachers',
        'Designers',
        'Steelers',
        'Shepperds'
    ]){
        console.log('The ' + adj + ' ' + noun);
    }
}