#include <stdio.h>
#include <string.h>
#include <espeak/speak_lib.h>

static void say(const char *text)
{
    static int initialized = 0;
    if (! initialized) {
        espeak_Initialize(AUDIO_OUTPUT_PLAYBACK, 0, NULL, 0);
        espeak_SetVoiceByName("en");
        initialized = 1;
    }
    espeak_Synth(text, strlen(text)+1,
                 0, POS_CHARACTER, 0,
                 espeakCHARS_UTF8, NULL, NULL);
    espeak_Synchronize();
}

int main()
{
    char text[1000];
    int i;

    for (i = 0; i < 5; ++i) {
        scanf("%s", text);
        say(text);
    }

    return 0;
}
