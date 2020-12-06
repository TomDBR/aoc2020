#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>

struct info {
	int s;		// stride
	int raw_s; 	// raw stride (plus newline)
	int row_s;	// row stride
	int col_s;	// col stride
	int nseat;	// seat count
	int file_sz;	// file size (in bytes)
	char *buffer;	// file buffer
};

void banic(const char *fmt, ...) {
	va_list ap;
	va_start(ap, fmt);
	vfprintf(stderr, fmt, ap);
	va_end(ap);
	if (fmt[0] && fmt[strlen(fmt)-1] == ':') {
		fputc(' ', stderr);
		perror(NULL);
	}
	exit(1);
}

void read_info(const char *filename, struct info *i)
{
	char c;
	int index = 0;
	FILE *f = fopen(filename, "r");
	if (!f) banic("fopen:");
	memset(i, 0, sizeof(*i));

	// find stride information (bitsize)
	while ((c = fgetc(f)) != '\n') {
		i->s++;
		i->row_s += c <= 'F'; // or B
		i->col_s += c >= 'L'; // or R
	}

	// find the filesize in bytes
	fseek(f, 0, SEEK_END);
	i->file_sz += ftell(f);
	fseek(f, 0, SEEK_SET);

	// divide filesz by (stride + newline) + stride
	i->nseat = ((i->file_sz - i->s) / (i->s + 1)) + 1;
	i->buffer = malloc((i->nseat * i->s) * sizeof(*i->buffer));
	if (!i->buffer) banic("malloc():");

	while ((c = fgetc(f)) != EOF) if (c != '\n') {
		i->buffer[index++] = c;
	}
	fclose(f);
}

void free_info(struct info *i)
{
	free(i->buffer);
}

int binary(char *b, int size, char target)
{
	int rv = 0;
	for (int i = 0; i < size; i++) {
		rv |= (b[i] == target) << ((size - 1) - i);
	}
	return rv;
}

int cmp(const void *left, const void *right)
{
	return *(int *)left - *(int *)right;
}

const char *const df_filename = "./input.txt";
int main(int argc, char **argv)
{
	struct info i;
	const char *filename = df_filename;
	if (argc > 1) filename = argv[1];
	read_info(filename, &i);

	char *seat;
	int part1 = -1;
	int seats[i.nseat];
	for (int j = 0; j < i.nseat; j++) {
		seat = i.buffer + (j * i.s);
		seats[j] = binary(seat, i.row_s, 'B') * (1 << i.col_s);
		seats[j] += binary(seat + i.row_s, i.col_s, 'R');
		if (seats[j] > part1) part1 = seats[j];
	}

	printf("part1: %i\npart2: [\n", part1);
	qsort(seats, i.nseat, sizeof(*seats), cmp);
	for (int j = 0; j < i.nseat - 1; j++) {
		if (seats[j] + 1 != seats[j + 1]) {
			printf("  %i,\n", seats[j] + 1);
		}
	}
	printf("]\n");

	free_info(&i);
	return 0;
}
