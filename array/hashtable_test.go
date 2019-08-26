package array

import (
	"fmt"
	"testing"
)

func TestCreate(t *testing.T) {
	m := newmap()
	for i := 0; i < mapsize; i++ {
		if m.store[i] != nil {
			t.Error("Non nil map on init")
		}
	}
}

func TestDump(t *testing.T) {
	m := newmap()
	m.Put("a", 1)
	m.Put("b", 1)
	dump := m.Dump()
	t.Log(dump)
	if dump == "" {
		t.Error("dump doesnt work properly")
	}
}

func TestHashFuncSimple(t *testing.T) {
	h1 := hashfuncSimple("a")
	h2 := hashfuncSimple("b")
	if h1 == 0 && h2 == 0 {
		t.Error("hash of 'a' and 'b' both produced 0")
	}
}

func TestGet(t *testing.T) {
	m := newmap()
	m.Put("a", 19)
	if v, _ := m.Get("a"); v != 19 {
		t.Errorf("put 'a', 19, got %d", v)
	}
	m.Put("a", 20)
	if v, _ := m.Get("a"); v != 20 {
		t.Errorf("put 'a', 20, got %d", v)
	}
	for i := 0; i < 1000; i++ {
		s := fmt.Sprintf("%d", i)
		m.Put(s, i)
	}
	t.Error(m.Dump())
}

func TestPut(t *testing.T) {
	m := newmap()
	m.Put("", 1)
	t.Error(m.Dump())
}
