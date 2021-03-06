// Implements a dictionary's functionality

#include <stdbool.h>
#include "dictionary.h"
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <strings.h>
#include <string.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N] = {NULL};
int sized =0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    node *ptr;
    ptr = table[hash(word)];
    while(ptr != NULL)
    {
        if(strcasecmp(ptr->word,word) ==0)
        {
            return true;
        }
        ptr = ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    if('A' <= word[0] && word[0] <= 'Z')
    {
        return word[0] - 'A';
    }
    else if ('a' <= word[0] && word[0] <= 'z')
    {
        return word[0] - 'a';
    }
    return 0;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary,"r");
    if (file == NULL)
    {
        return false;
    }
    printf("Loading, Please wait ... \n");
    char dic[LENGTH +1];
    while (fscanf ( file, "%s", dic) != EOF){
    node *n = malloc(sizeof(node));
    strcpy(n->word, dic);
    n->next = table[hash(dic)];
    table[hash(dic)] = n;
    sized++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return sized;

}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    int count =0;

    node *tmp;
    node *ptr;
    for(int i=0; i<N;i++){
        ptr = table[i];
        tmp = ptr;
        if(ptr != NULL){
            count++;
        }
        while(ptr != NULL){
            ptr = ptr->next;
            free(tmp);
            tmp = ptr;
        }

    }
    if(count ==0){
        return false;
    }else{


       return true;
    }
}
