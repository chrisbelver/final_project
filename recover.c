#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int BLOCK = 512;

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Create a buffer
    uint8_t buffer[BLOCK];

    int jpeg_count = 0;

    char filename[8];

    FILE *img = NULL;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, BLOCK, card) == BLOCK)
    {
        // Create JPEGs from the data
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {
            if (jpeg_count == 0)
            {
                sprintf(filename, "%03i.jpg", jpeg_count);

                img = fopen(filename, "w");
                fwrite(&buffer, 1, BLOCK, img);
                jpeg_count++;
            }
            else
            {
                fclose(img);

                sprintf(filename, "%03i.jpg", jpeg_count);

                img = fopen(filename, "w");
                fwrite(&buffer, 1, BLOCK, img);
                jpeg_count++;
            }
        }
        else
        {
            if (jpeg_count != 0)
            {
                fwrite(&buffer, 1, BLOCK, img);
            }
        }

    }
    fclose(card);
    fclose(img);
}
