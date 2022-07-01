<template>
  <div class="home">
    <h3 v-if="books && booksread">Books</h3>
    <ul>
      <li v-for="book in books" :key="book.id">
        {{ `${book.title} - ${book.price} - ${bookreview(book.id)}` }}
      </li>
    </ul>

    <h3 v-if="readers">Readers</h3>
    <ul v-if="booksread">
      <li v-for="reader in readers" :key="reader.id">
        {{ `${reader.name} has read: ${booksread.filter((b) => b.reader === reader.id).length} book(s)` }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { get_books, get_readers, get_read_books } from '@/services/api-service'
import HelloWorld from '@/components/HelloWorld.vue' // @ is an alias to /src

@Component({
  components: {
    HelloWorld,
  },
})
export default class HomeView extends Vue {
  books = 'test'
  readers = null
  booksread: any[] = []

  bookreview(book_id: number) {
    if (book_id) {
      let booksread = this.booksread.filter((book) => {
        return book.book === book_id
      })
      return booksread[0].review
    }
  }

  mounted() {
    get_read_books().then((booksread) => {
      this.booksread = booksread
    })
    get_books().then((books) => {
      this.books = books
    })
    get_readers().then((readers) => {
      this.readers = readers
    })
  }
}
</script>
