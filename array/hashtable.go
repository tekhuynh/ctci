package array

import (
	"errors"
	"fmt"
)

/*
Hash table is a data structure which maps keys to values.
- In: key, Out: value or nil
- In: key value, Out: nil

key: Hash(key) -> index
value: Storage(index) -> value
	   Storage(index, value) -> nil

Hash: do math on key
Storage: make space if needed and store at index
         retrieve value from given index

*/
const mapsize = 100

func hashfuncSimple(s string) int32 {
	index := int32(0)
	for i, runeValue := range s {
		index += int32(i+1) * runeValue * 7
	}
	return index
}

type hashmap struct {
	store    [mapsize]*mapitem
	hashfunc func(s string) int32
}

func newmap() *hashmap {
	return &hashmap{[mapsize]*mapitem{}, hashfuncSimple}
}

func (h *hashmap) Get(key string) (value int, err error) {
	mapitem := h.store[h.hashfunc(key)%100]
	for i := mapitem; i != nil; i = i.next {
		if mapitem.key == key {
			return i.value, nil
		}
	}
	return 0, errors.New("key not found")
}

func (h *hashmap) Put(key string, value int) {
	index := h.hashfunc(key) % 100
	mi := h.store[index]

	if mi == nil {
		h.store[index] = &mapitem{key, value, nil}
		return
	}

	var last *mapitem
	for ; mi != nil; mi = mi.next {
		if mi.key == key {
			mi.value = value
			return
		}
		last = mi
	}

	last.next = &mapitem{key, value, nil}
}

func (h *hashmap) Dump() string {
	dump := ""
	for i := 0; i < mapsize; i++ {
		dump += fmt.Sprintf("%d:\n", i)
		for j := h.store[i]; j != nil; j = j.next {
			dump += fmt.Sprintf("\t%s: %d\n", j.key, j.value)
		}
	}
	return dump
}

type mapitem struct {
	key   string
	value int
	next  *mapitem
}
