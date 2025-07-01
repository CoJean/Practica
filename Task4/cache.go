package cache

// Cache reprezintă un cache simplu FIFO cu capacitate limitată.
type Cache struct {
	capacity int
	data     map[string]string
	keys     []string
}

// NewCache creează un cache nou cu capacitatea specificată.
func NewCache(capacity int) *Cache {
	return &Cache{
		capacity: capacity,
		data:     make(map[string]string),
		keys:     make([]string, 0, capacity),
	}
}

// Get returnează valoarea stocată și dacă a fost găsită.
func (c *Cache) Get(key string) (string, bool) {
	val, found := c.data[key]
	return val, found
}

// Put adaugă o valoare în cache și elimină cea mai veche dacă depășește capacitatea.
func (c *Cache) Put(key, value string) {
	if _, exists := c.data[key]; exists {
		c.data[key] = value
		return
	}

	if len(c.keys) >= c.capacity {
		oldest := c.keys[0]
		c.keys = c.keys[1:]
		delete(c.data, oldest)
	}

	c.keys = append(c.keys, key)
	c.data[key] = value
}
